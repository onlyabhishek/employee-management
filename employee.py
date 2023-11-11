import streamlit as st
import mysql.connector
import pandas as pd

# Establish a connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhi@2608",
    database="employee"
)
mycursor = mydb.cursor()

def create_record():
    st.subheader("Create a Record")
    EmployeeId = st.text_input("Enter Employee Id")
    firstname = st.text_input("Enter the First Name")
    lastname = st.text_input("Enter the Last Name")
    salary = st.text_input("Enter the Salary")
    email = st.text_input("Enter the Email")
    
    if st.button("Create"):
        try:
            sql = "INSERT INTO employee (EmployeeId, firstname, lastname, salary, email) VALUES (%s, %s, %s, %s, %s)"
            val = (EmployeeId, firstname, lastname, salary, email)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")
    else:
        st.warning("Record not created")

def read_records():
    st.subheader("Read Records")
    mycursor.execute("SELECT * FROM employee")
    result = mycursor.fetchall()
    if result:
        df = pd.DataFrame(result, columns=["EmployeeID", "FirstName", "LastName", "Salary", "Email"])
        st.dataframe(df)
    else:
        st.write("No records found.")

    mycursor.execute("SELECT count(EmployeeID) FROM employee")
    result_count = mycursor.fetchone()
    print(result_count)
    count = result_count[0] if result_count else 0
    st.subheader(f"Count the number of Employee: {count}")

def update_record():
    st.subheader("Update a Record")
    EmployeeId = st.text_input("Enter Employee Id")
    new_firstname = st.text_input("Enter the New First Name")
    new_lastname = st.text_input("Enter the New Last Name")
    new_salary = st.text_input("Enter the New Salary")
    new_email = st.text_input("Enter the New Email")
    if st.button("Update"):
        try:
            sql = "UPDATE employee SET firstname=%s, lastname=%s, salary=%s, email=%s WHERE EmployeeId=%s"
            val = (new_firstname, new_lastname, new_salary, new_email, EmployeeId)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def delete_record():
    st.subheader("Delete a Record")
    EmployeeId = st.text_input("Enter Employee Id to delete")
    if st.button("Delete"):
        try:
            sql = "DELETE FROM employee WHERE EmployeeId=%s"
            val = (EmployeeId,)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def main():
    st.title("Employee")
    option = st.sidebar.selectbox("Select an operation", ("Create", "Read", "Update", "Delete"))
    
    if option == "Create":
        create_record()
    elif option == "Read":
        read_records()
    elif option == "Update":
        update_record()
    elif option == "Delete":
        delete_record()

if __name__ == "__main__":
    main()
