import pandas as pd

# VII Semester

# ignored seminar
it7a = {
    "section": "IT7A",
    "location" : 317,
    "teachers" : ["Giridhar Kamath", "Anju", "Pooja S."],
    "teachers_initial" : ["GK", "ANR", "PS"],
    "courses" : ["Essentials of Management", "Business Intelligence", "Information and Web Security"],
    "courses_initial" : ["EOM", "BI", "IWS"],
    "courses_codes" : ["HUM 4001", "ICT 4101", "ICT 4102"],
    "labs" : ["DA Lab A", "DA Lab B"],
    "lab_locations": [8,8],
    "lab_faculty_initials": ["PS", "IP"],
    "course_count" : [3,4,3]
}

it7b = {
    "section": "IT7B",
    "location" : 315,
    "teachers" : ["Pooja Kini", "Swathi B.P", "Krishna Prakasha"],
    "teachers_initial" : ["PK", "SB", "KP"],
    "courses" : ["Essentials of Management", "Business Intelligence", "Information and Web Security"],
    "courses_initial" : ["EOM", "BI", "IWS"],
    "courses_codes" : ["HUM 4001", "ICT 4101", "ICT 4102"],
    "labs" : ["DA Lab A", "DA Lab B"],
    "lab_locations": [8,8],
    "lab_faculty_initials": ["SB", "PS"],
    "course_count" : [3,4,3]
}

cce7a = {
    "section": "CCE7A",
    "location" : 311,
    "teachers" : ["Giridhar Kamath", "Krishna Prakasha", "Santosh Kamath"],
    "teachers_initial" : ["GK", "KP", "SAK"],
    "courses" : ["Essentials of Management", "Cyber Security", "Wireless Sensor and Adhoc Networks"],
    "courses_initial" : ["EOM", "CyS", "WSAN"],
    "courses_codes" : ["HUM 4001", "ICT 4102", "ICT 4151"],
    "labs" : ["ND&WSAN Lab A", "ND&WSAN Lab B"],
    "lab_locations": [8,8],
    "lab_faculty_initials": ["JY", "CHS"],
    "course_count" : [3,3,4]
}

cce7b = {
    "section": "CCE7B",
    "location" : 313,
    "teachers" : ["A Vittaleswar", "Nisha P Shetty", "Santosha Rao"],
    "teachers_initial" : ["AV", "NS", "SR"],
    "courses" : ["Essentials of Management", "Cyber Security", "Wireless Sensor and Adhoc Networks"],
    "courses_initial" : ["EOM", "CyS", "WSAN"],
    "courses_codes" : ["HUM 4001", "ICT 4102", "ICT 4151"],
    "labs" : ["ND&WSAN Lab A", "ND&WSAN Lab B"],
    "lab_locations": [8,8],
    "lab_faculty_initials": ["VK", "CHS"],
    "course_count" : [3,3,4]
}


pe7 = {
    "section": "PE7",
    "courses": ["PE IV", "PE V", "PE VI"],
    "courses_initial": ["PE4", "PE5", "PE6"],
    "courses_codes" : ["ICT 4019", "ICT 4011", "ICT 4008"],
    "location": 311,
    "teachers": ["Sangeeta T.S.", "Ajitha Shenoy", "Chethan Sharma"],
    "teachers_initial": ["STS", "AS", "CHS"],
    "course_count": [3,3,3]
}

# V Semester

it5a = {
    "section": "IT5A",
    "location" : 315,
    "teachers" : ["Smitha Pai", "Santosh Kamath", "Aiswarya", "Poornalatha G."],
    "teachers_initial" : ["SP", "SAK", "AB", "PG"],
    "courses" : ["Operating Systems", "Embedded Systems", "Internet Tools & Technology", "Design and Aalysis of Algorithms"],
    "courses_initial" : ["OS", "ES", "ITT", "DAA"],
    "courses_codes" : ["ICT 3101", "ICT 3102", "ICT 3103", "ICT 3107"],
    "labs" : ["ES Lab A", "ES Lab B", "ITT Lab A", "ITT Lab B", "OS Lab A", "OS Lab B"],
    "lab_locations": [2,2,8,3,8,8],
    "lab_faculty_initials": ["SAK", "IP", "AB", "DO", "AMJ", "RA"],
    "course_count" : [4,4,3,4]
}

it5b = {
    "section": "IT5B",
    "location" : 317,
    "teachers" : ["Anusha Hegde", "Santosha Rao", "Sirish Shetty B", "Poornalatha G."],
    "teachers_initial" : ["AH", "SR", "SSB", "PG"],
    "courses" : ["Operating Systems", "Embedded Systems", "Internet Tools & Technology", "Design and Aalysis of Algorithms"],
    "courses_initial" : ["OS", "ES", "ITT", "DAA"],
    "courses_codes" : ["ICT 3101", "ICT 3102", "ICT 3103", "ICT 3107"],
    "labs" : ["ES Lab A", "ES Lab B", "ITT Lab A", "ITT Lab B", "OS Lab A", "OS Lab B"],
    "lab_locations": [2,2,5,2,8,8],
    "lab_faculty_initials": ["IP", "AKC", "RH", "AH", "VB", "AH"],
    "course_count" : [4,4,3,4]
}


cce5a= {
    "section": "CCE5A",
    "location" : 311,
    "teachers_initial" : ["MB", "RG", "RH", "DO", "AB"],
    "courses_initial" : ["FAAD", "HSCN", "PP", "DBS", "SDT"],
    "courses_codes" : ["ICT 3151", "ICT 3152", "ICT 3153", "ICT 3154", "ICT 3155"],
    "labs" : ["RUP Lab A", "RUP Lab B", "DBS Lab A", "DBS Lab B"],
    "lab_locations": [5,5,1,1],
    "lab_faculty_initials": ["CP", "SAC", "DO", "ACV"],
    "course_count" : [3,4,3,3,3]
}

cce5b= {
    "section": "CCE5B",
    "location" : 313,
    "teachers_initial" : ["MB", "RG", "RH", "SAC", "SK"],
    "courses_initial" : ["FAAD", "HSCN", "PP", "DBS", "SDT"],
    "courses_codes" : ["ICT 3151", "ICT 3152", "ICT 3153", "ICT 3154", "ICT 3155"],
    "labs" : ["RUP Lab A", "RUP Lab B", "DBS Lab A", "DBS Lab B"],
    "lab_locations": [5,5,1,1],
    "lab_faculty_initials": ["RJ", "RG", "SAC", "SK"],
    "course_count" : [3,4,3,3,3]
}

pe1 = {
    "section": "PE1",
    "courses": ["PE I"],
    "courses_initial": ["PE1"],
    "location": 311,
    "courses_codes" : ["ICT 4006"],
    "teachers": ["K. Rajesh Rao"],
    "teachers_initial": ["RJ"],
    "course_count": [3]
}

cce3b= {
    "section": "CCE3B",
    "location" : 213,
    "teachers_initial" : ["SHK", "VK", "DS", "RA", "CP"],
    "courses_initial" : ["Maths", "DS", "DSCO", "OOP", "PDC"],
    "courses_codes" : ["MAT 2155", "ICT 2151", "ICT 2155", "ICT 2153", "ICT 2154"],
    "labs" : ["DS Lab A", "DS Lab B", "OOP Lab A", "OOP Lab B", "DSD Lab A", "DSD Lab B"],
    "lab_locations": [3,3,3,3,9,9],
    "lab_faculty_initials": ["VK", "CHS", "CP", "STS", "ACV", "PS"],
    "course_count" : [3,4,4,4,4]
}

cce3a= {
    "section": "CCE3A",
    "location" : 214,
    "teachers_initial" : ["KAB", "AKC", "RN", "AR", "IP"],
    "courses_initial" : ["Maths", "DS", "DSCO", "OOP", "PDC"],
    "courses_codes" : ["MAT 2155", "ICT 2151", "ICT 2155", "ICT 2153", "ICT 2154"],
    "labs" : ["DS Lab A", "DS Lab B", "OOP Lab A", "OOP Lab B", "DSD Lab A", "DSD Lab B"],
    "lab_locations": [4,4,1,5,9,9],
    "lab_faculty_initials": ["AKC", "RG", "MB", "SK", "RN", "AH"],
    "course_count" : [3,4,4,4,4]
}

it3a= {
    "section": "IT3A",
    "location" : 215,
    "teachers_initial" : ["MKJ", "MS", "DS", "SSB", "VB"],
    "courses_initial" : ["Maths", "DS", "DSD", "OOP", "PDC"],
    "courses_codes" : ["MAT 2155", "ICT 2151", "ICT 2152", "ICT 2153", "ICT 2154"],
    "labs" : ["DS Lab A", "DS Lab B", "OOP Lab A", "OOP Lab B", "DSM Lab A", "DSM Lab B"],
    "lab_locations": [3,3,1,1,9,9],
    "lab_faculty_initials": ["VB", "NS", "SSB", "CP", "DS", "PS"],
    "course_count" : [3,4,4,4,4]
}

it3b= {
    "section": "it3A",
    "location" : 216,
    "teachers_initial" : ["KK", "JY", "RN", "CK", "RA"],
    "courses_initial" : ["Maths", "DS", "DSD", "OOP", "PDC"],
    "courses_codes" : ["MAT 2155", "ICT 2151", "ICT 2152", "ICT 2153", "ICT 2154"],
    "labs" : ["DS Lab A", "DS Lab B", "OOP Lab A", "OOP Lab B", "DSM Lab A", "DSM Lab B"],
    "lab_locations": [3,3,3,1,9,9],
    "lab_faculty_initials": ["JY", "SB", "NS", "ANR", "RJ", "PS"],
    "course_count" : [3,4,4,4,4]
}

all_sec = [it7a, it7b, cce7a, cce7b, pe7, it5a, it5b, cce5a, cce5b, pe1, it3a, it3b, cce3a, cce3b]

# semester_course_mapping.csv, teacher
df = pd.read_csv('ready/teachers_final.csv')
programme = []
dept = []
sem = []
code = []
section = []
credits = []
course_name = []
course_code = []
course_abbreviation = []
course_credits = []
course_duration = []
course_type = []
course_department = []
course_max = []
type = []
extra=[]
teacher = []
location = []
for x in [it7a,it7b,cce7a,cce7b,pe7]:
    try :
        a = x["lab_locations"]
        for a in x["teachers_initial"]:
            reg_no = df.loc[df['First Name'] == a, 'Registration Number'].iloc[0]
            teacher.append(reg_no)
            section.append(x["section"])
        for a in x["courses_initial"]:
            course_name.append(a)
            programme.append("B.Tech.")
            type.append("Theory")
            sem.append(7)
            course_abbreviation.append(a)
        for a in x["courses_codes"]:
            course_code.append(a)
            course_department.append(a[:3])
        for a in x["course_count"]:
            course_credits.append(a)
            course_type.append("Mandatory")
            course_max.append(70)
            course_duration.append(60)
            extra.append("")
            location.append(x["location"])
        
        for a in x["labs"]:
            course_duration.append(180)
            course_max.append(35)
            type.append("Lab")
            programme.append("B.Tech.")
            sem.append(7)
            course_credits.append(2)
            course_type.append("Mandatory")
            course_name.append(a)
            course_abbreviation.append(a.replace(" ", ""))
            extra.append("")
            course_department.append("ICT")
            index = a.find(" ")
            if index != -1:
                characters_before_space = a[:index]
            else:
                characters_before_space = a
            course_code.append(characters_before_space + x["courses_codes"][0][4])
        for a in x["lab_faculty_initials"]:
            reg_no = df.loc[df['First Name'] == a, 'Registration Number'].iloc[0]
            teacher.append(reg_no) 
            section.append(x["section"])
        for a in x["lab_locations"]:
            location.append(a)
    except:
        for a in x["courses_initial"]:
            course_name.append(a)
            course_abbreviation.append(a)
        for a in x["courses_codes"]:
            course_code.append(a)
            sem.append(7)
            course_department.append(a[:3])
        for a in x["course_count"]:
            programme.append("B.Tech.")
            course_credits.append(a)
            course_type.append("Programme Elective")
            course_max.append(70)
            type.append("Theory")
            course_duration.append(60)
            extra.append("")
            location.append(x["location"])
        for a in x["teachers_initial"]:
            reg_no = df.loc[df['First Name'] == a, 'Registration Number'].iloc[0]
            teacher.append(reg_no)
            section.append(x["section"])

# print(len(teacher), len(location), len(course_code))

# for x in [it5a,it5b,cce5a,cce5b,pe1]:
#     try :
#         a = x["lab_locations"]
#         for a in x["teachers_initial"]:
#             reg_no = df.loc[df['First Name'] == a, 'Registration Number'].iloc[0]
#             teacher.append(reg_no)
#             section.append(x["section"])
#         for a in x["courses_initial"]:
#             course_name.append(a)
#             programme.append("B.Tech.")
#             type.append("Theory")
#             sem.append(5)
#             course_abbreviation.append(a)
#         for a in x["courses_codes"]:
#             course_code.append(a)
#             course_department.append(a[:3])
#         for a in x["course_count"]:
#             course_credits.append(a)
#             course_type.append("Mandatory")
#             course_max.append(70)
#             course_duration.append(60)
#             extra.append("")
#             location.append(x["location"])
        
#         for a in x["labs"]:
#             course_duration.append(180)
#             course_max.append(35)
#             type.append("Lab")
#             programme.append("B.Tech.")
#             sem.append(5)
#             course_credits.append(2)
#             course_type.append("Mandatory")
#             course_name.append(a)
#             course_abbreviation.append(a.replace(" ", ""))
#             extra.append("")
#             course_department.append("ICT")
#             index = a.find(" ")
#             if index != -1:
#                 characters_before_space = a[:index]
#             else:
#                 characters_before_space = a
#             course_code.append(characters_before_space + x["courses_codes"][0][4])
#         for a in x["lab_faculty_initials"]:
#             reg_no = df.loc[df['First Name'] == a, 'Registration Number'].iloc[0]
#             teacher.append(reg_no) 
#             section.append(x["section"])
#         for a in x["lab_locations"]:
#             location.append(a)
#     except:
#         for a in x["courses_initial"]:
#             course_name.append(a)
#             course_abbreviation.append(a)
#         for a in x["courses_codes"]:
#             course_code.append(a)
#             sem.append(5)
#             course_department.append(a[:3])
#         for a in x["course_count"]:
#             programme.append("B.Tech.")
#             course_credits.append(a)
#             course_type.append("Programme Elective")
#             course_max.append(70)
#             type.append("Theory")
#             course_duration.append(60)
#             extra.append("")
#             location.append(x["location"])
#         for a in x["teachers_initial"]:
#             reg_no = df.loc[df['First Name'] == a, 'Registration Number'].iloc[0]
#             teacher.append(reg_no)
#             section.append(x["section"])

# print(len(teacher), len(location), len(course_code))

# for x in [it3a,it3b,cce3a,cce3b]:
#     try :
#         a = x["lab_locations"]
#         for a in x["teachers_initial"]:
#             reg_no = df.loc[df['First Name'] == a, 'Registration Number'].iloc[0]
#             teacher.append(reg_no)
#             section.append(x["section"])
#         for a in x["courses_initial"]:
#             course_name.append(a)
#             programme.append("B.Tech.")
#             type.append("Theory")
#             sem.append(3)
#             course_abbreviation.append(a)
#         for a in x["courses_codes"]:
#             course_code.append(a)
#             course_department.append(a[:3])
#         for a in x["course_count"]:
#             course_credits.append(a)
#             course_type.append("Mandatory")
#             course_max.append(70)
#             course_duration.append(60)
#             extra.append("")
#             location.append(x["location"])
        
#         for a in x["labs"]:
#             course_duration.append(180)
#             course_max.append(35)
#             type.append("Lab")
#             programme.append("B.Tech.")
#             sem.append(3)
#             course_credits.append(2)
#             course_type.append("Mandatory")
#             course_name.append(a)
#             course_abbreviation.append(a.replace(" ", ""))
#             extra.append("")
#             course_department.append("ICT")
#             index = a.find(" ")
#             if index != -1:
#                 characters_before_space = a[:index]
#             else:
#                 characters_before_space = a
#             course_code.append(characters_before_space + x["courses_codes"][0][4])
#         for a in x["lab_faculty_initials"]:
#             reg_no = df.loc[df['First Name'] == a, 'Registration Number'].iloc[0]
#             teacher.append(reg_no) 
#             section.append(x["section"])
#         for a in x["lab_locations"]:
#             location.append(a)
#     except:
#         for a in x["courses_initial"]:
#             course_name.append(a)
#             course_abbreviation.append(a)
#         for a in x["courses_codes"]:
#             course_code.append(a)
#             sem.append(3)
#             course_department.append(a[:3])
#         for a in x["course_count"]:
#             programme.append("B.Tech.")
#             course_credits.append(a)
#             course_type.append("Programme Elective")
#             course_max.append(70)
#             type.append("Theory")
#             course_duration.append(60)
#             extra.append("")
#             location.append(x["location"])
#         for a in x["teachers_initial"]:
#             reg_no = df.loc[df['First Name'] == a, 'Registration Number'].iloc[0]
#             teacher.append(reg_no)
#             section.append(x["section"])
print(len(teacher), len(location), len(course_code))

building_name = []
floor_number = []
for i in range(len(teacher)):
    building_name.append("AB5")
    floor_number.append(3)

courses = {"Registration Number": teacher, "Course Code": course_code, "Building Name": building_name, "Floor Number": floor_number, "Room Name": location,	"Section": section	 ,"Semester": sem, "Programme": programme, "Department": course_department}
print(len(teacher), len(course_code), len(building_name), len(floor_number), len(location), len(section), len(section), len(sem), len(programme), len(course_department))
df_courses = pd.DataFrame(courses)
df_courses.to_csv("teacher_course_location_section_mapping_final.csv", index=False)

# courses.csv
# course_name = []
# course_code = []
# course_abbreviation = []
# course_credits = []
# course_duration = []
# course_type = []
# course_department = []
# course_max = []
# type = []
# extra=[]
# for x in all_sec:
#     try :
#         a = x["lab_locations"]
#         for a in x["courses_initial"]:
#             course_name.append(a)
#             type.append("Theory")
#             course_abbreviation.append(a)
#         for a in x["courses_codes"]:
#             course_code.append(a)
#             course_department.append(a[:3])
#         for a in x["course_count"]:
#             course_credits.append(a)
#             course_type.append("Mandatory")
#             course_max.append(70)
#             course_duration.append(60)
#             extra.append("")
        
#         for a in x["labs"]:
#             course_duration.append(180)
#             course_max.append(35)
#             type.append("Lab")
#             course_credits.append(2)
#             course_type.append("Mandatory")
#             course_name.append(a)
#             course_abbreviation.append(a.replace(" ", ""))
#             extra.append("")
#             course_department.append("ICT")
#             index = a.find(" ")
#             if index != -1:
#                 characters_before_space = a[:index]
#             else:
#                 characters_before_space = a
#             course_code.append(characters_before_space + x["courses_codes"][0][4])
#     except:
#         for a in x["courses_initial"]:
#             course_name.append(a)
#             course_abbreviation.append(a)
#         for a in x["courses_codes"]:
#             course_code.append(a)
#             course_department.append(a[:3])
#         for a in x["course_count"]:
#             course_credits.append(a)
#             course_type.append("Programme Elective")
#             course_max.append(70)
#             type.append("Theory")
#             course_duration.append(60)
#             extra.append("")

# courses = {"Name": course_name, "Code": course_code, "Abbreviation": course_abbreviation, "Duration": course_duration, "Maximum Student Capacity": course_max, "Type": type, "Credits": course_credits,	"Department": course_department, "Elective Type": course_type, "Elective Generic Name": extra,	"Elective Generic Code": extra}
# print(len(course_name), len(course_code), len(course_abbreviation), len(course_duration), len(course_max), len(type), len(course_credits), len(course_department), len(course_type), len(extra))
# df_courses = pd.DataFrame(courses)
# df_courses.to_csv("courses_final.csv", index=False)

# teachers.csv

# abbreviation = []
# name = []
# registration = []
# phone = []
# email = []
# count = 0
# seniority = []
# department = []
# for x in all_sec:
#     for y in x["teachers_initial"]:
#         abbreviation.append(y)

# teachers = { "Abbreviation": abbreviation}
# df_teachers = pd.DataFrame(teachers)
# df_teachers.drop_duplicates()

# abbreviation = []
# name = []
# email = []
# seniority = []
# department = []
# for x in df_teachers['Abbreviation']:
#     abbreviation.append(x)
#     name.append(x)
#     email.append(x+"@gmail.com")
#     seniority.append(1)
#     department.append("ICT")
#     count+=1
#     registration.append("EMP0"+str(count)) 
#     phone.append(count)

# teachers = {"Registration Number" : registration, "Seniority Level": seniority,	"Department": department, "First Name": name, "Middle Name": name,	"Last Name": name, "Abbreviation": name, "Email": email, "Phone": phone}
# df_teachers = pd.DataFrame(teachers)
# df_teachers.drop_duplicates()

# df_teachers.to_csv('teachers_final.csv', index=False)



