grades=[[5,4,3],[2,5],[4]]
def flatten_grades(grades):
    result=[]
    for x in grades:
        result.extend(x)
    print(result)
# print(flatten_grades(grades))

grades = (6, 3, 4, 5)
def top_two(grades):
    sorted_grades = sorted(grades)
    return tuple(sorted_grades[-2:])
# print(top_two(grades))
                

students = {"Alice": [5, 4, 3], "Bob": [2, 5, 4]}
def average_score(students):
    for name in students:
        students[name]=sum(students[name])/len(students[name])
    print(students)
# print(average_score(students))

def unique_subjects(*grades_lists):
    a=set()
    for x in grades_lists:
        a.update(x)
    print(a)
# print(unique_subjects(["Math", "Bio"], ["Bio", "PE"]))

ids = [1, 2, 4]
def  flag_students(ids):
    a = 0
    for i in ids:
        a =  a| i
    return a
# print(flag_students([1,2,4]))

names = ["Ann", "Борис"]
def encode_names(names):
    result=[]
    name=[]
    for i in names:
        for j in i:
            name.append(ord(j))
        result.append(name)
        name=[]
    return(result)
# print(encode_names(names))
int(), float(), bool(), str()
list(), dict(), set(), frozenset(), tuple()
p = 3,14
print(int(p), float(p), bool(p), str(p),list(p), dict(p), set(p), frozenset(p), tuple(p))





    









    


