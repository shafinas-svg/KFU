import pandas as pd

# Часть 1. Создание класса и подготовка данных
class AdvancedStudentAnalytics:

    def __init__(self, df):
        self.df = df.copy()
        self._prepare_data()

    def _prepare_data(self):
        #Заполнить project_score медианой
        self.df["project_score"] = self.df["project_score"].fillna(
            self.df["project_score"].median()
        )

        #Создать столбец average_grade
        self.df["average_grade"] = self.df[["math", "physics", "cs"]].mean(axis=1)

        #Создать performance_level:
        def get_performance_level(avg):
            if avg >= 85:
                return "high"
            elif avg >= 70:
                return "medium"
            else:
                return "low"

        self.df["performance_level"] = self.df["average_grade"].apply(get_performance_level)

        #Создать risk_level:
        def get_risk_level(row):
            if row["attendance"] < 60 or row["average_grade"] < 65:
                return "high risk"
            elif 60 <= row["attendance"] <= 75:
                return "medium risk"
            else:
                return "low risk"

        self.df["risk_level"] = self.df.apply(get_risk_level, axis=1)

# Часть 2. Методы класса
    def top_students(self, n):
        return self.df.sort_values(by="average_grade", ascending=False).head(n)


    def group_stats(self):
        stats = self.df.groupby("group").agg({
            "average_grade": "mean",
            "attendance": "mean",
            "name": "count"
        })

        stats = stats.rename(columns={
            "attendance": "average_attendance",
            "name": "student_count"
        })

        return stats

    def at_risk_students(self):
        return self.df[self.df["risk_level"] == "high risk"]

    def scholarship_analysis(self):
        return self.df.groupby("scholarship").agg({
            "average_grade": "mean",
            "attendance": "mean"
        })

    def city_performance(self):
        city_avg = self.df.groupby("city")["average_grade"].mean()

        best_city = city_avg.idxmax()
        worst_city = city_avg.idxmin()

        return {
            "best_city": best_city,
            "worst_city": worst_city
        }

    def hidden_top_students(self):
        return self.df[
            (self.df["average_grade"] > 85) &
            (self.df["scholarship"] == False)
        ]

    def lazy_geniuses(self):
        return self.df[
            (self.df["average_grade"] > 85) &
            (self.df["attendance"] < 60)
        ]
# Часть 3. Метод-композиция
    def full_analysis(self):
        city_info = self.city_performance()

        return {
            "top_3_students": self.top_students(3),
            "group_stats": self.group_stats(),
            "high_risk_count": len(self.at_risk_students()),
            "hidden_top_students_count": len(self.hidden_top_students()),
            "lazy_geniuses_count": len(self.lazy_geniuses()),
            "best_city": city_info["best_city"],
            "worst_city": city_info["worst_city"],
            "scholarship_analysis": self.scholarship_analysis()
        }
    
# Часть 4. Использование
import pandas as pd

df = pd.read_csv("students_extended.csv")

analytics = AdvancedStudentAnalytics(df)

print("Топ-3 студентов по среднему баллу:")
print(analytics.top_students(3))

print("\nСтатистика по группам:")
print(analytics.group_stats())

print("\nПолный анализ:")
print(analytics.full_analysis())