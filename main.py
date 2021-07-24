# This is a sample Python script.
import pandas as pd

def read_excel_by_file_path(file_path):
    print("*" * 30+" read excel from file path "+"*" * 30)
    dataframe = pd.read_excel(file_path,sheet_name=0)
    print(dataframe)
    return dataframe

def read_info_from_dataframe(dataframe):
    print("*" * 30 + " read excel info from dataframe " + "*" * 30)
    print(dataframe.info())
    print("Entry number: "+ str(len(dataframe)))

def read_cell_from_dataframe(dataframe,cell_index):
    print("*" * 30 + " read cell from dataframe " + "*" * 30)
    print(dataframe[cell_index["col"]][cell_index["row"]])

def print_all_students_name(dataframe):
    print("*" * 30 + " print all students name " + "*" * 30)
    print(dataframe["Name"])

def print_all_students_name_and_grade(dataframe):
    print("*" * 30 + " print all students name and grade " + "*" * 30)
    print(dataframe[["Name", "Grade"]])

def print_all_students_over_70(dataframe):
    print("*" * 30 + " print all students whose grade is over 70 " + "*" * 30)
    for index, row in dataframe.iterrows():
        if row['Grade'] >= 70:
            print(row['Name'], row['Grade'])

def print_all_students_class_4(dataframe):
    print("*" * 30 + " print all students who is in 六年四班 " + "*" * 30)
    for index, row in dataframe.iterrows():
        if row['Class'] == "六年四班":
            print(row['Name'], row['Class'], row['Grade'])

def print_all_female_students(dataframe):
    print("*" * 30 + " print all students who is female " + "*" * 30)
    for index, row in dataframe.iterrows():
        if row['Gender'] == "女":
            print(row['Name'], row['Class'], row['Gender'], row['Grade'])

def print_the_best_student(dataframe):
    print("*" * 30 + " print all students who has the highest grade " + "*" * 30)
    best_student = dataframe.iloc[0]
    for index, row in dataframe.iterrows():
        if row["Grade"] > best_student["Grade"]:
            best_student = row
    print(best_student)

if __name__ == '__main__':
    file_path = r'C:\Users\OPPO\Desktop\Jola_Python_Lerning\File_IO\src\data.xlsx'
    dataframe = read_excel_by_file_path(file_path)
    read_info_from_dataframe(dataframe)
    read_cell_from_dataframe(dataframe,{"col":"Class","row":3})
    print_all_students_name(dataframe)
    print_all_students_name_and_grade(dataframe)
    print_all_students_over_70(dataframe)
    print_all_students_class_4(dataframe)
    print_all_female_students(dataframe)
    print_the_best_student(dataframe)



