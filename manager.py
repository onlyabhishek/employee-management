import streamlit as st
import mysql.connector
import pandas as pd

# Establish a database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhi@2608",
    database="employee"
)
mycursor = mydb.cursor()

def read_records():
    st.subheader("Read Records")
    mycursor.execute("SELECT * FROM manager")
    result = mycursor.fetchall()
    if result:
        df = pd.DataFrame(result, columns=["ManagerID", "EmployeeID", "Email", "FirstName", "LastName"])
        st.dataframe(df)
    else:
        st.write("No records found.")

def create_record():
    st.subheader("Create a Record")
    ManagerID = st.text_input("Enter ManagerID")
    EmployeeID = st.text_input("Enter EmployeeID")
    Email = st.text_input("Enter Email")
    FirstName = st.text_input("Enter First Name")
    LastName = st.text_input("Enter Last Name")

    if st.button("Create"):
        try:
            # Modify the SQL query and values to match your table and columns (manager table)
            sql = "INSERT INTO manager (ManagerID, EmployeeID, Email, FirstName, LastName) VALUES (%s, %s, %s, %s, %s)"
            val = (ManagerID, EmployeeID, Email, FirstName, LastName)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def update_record():
    st.subheader("Update a Record")
    EmployeeID = st.text_input("Enter EmployeeID of the record to update")
    new_manager_id = st.text_input("Enter the new ManagerID")
    new_email = st.text_input("Enter the new Email")
    new_first_name = st.text_input("Enter the new First Name")
    new_last_name = st.text_input("Enter the new Last Name")

    if st.button("Update"):
        try:
            # Modify the SQL query to update the record with the specified EmployeeID
            sql = "UPDATE manager SET ManagerID = %s, Email = %s, FirstName = %s, LastName = %s WHERE EmployeeID = %s"
            val = (new_manager_id, new_email, new_first_name, new_last_name, EmployeeID)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def delete_record():
    st.subheader("Delete a Record")
    ManagerID = st.text_input("Enter ManagerID of the record to delete")

    if st.button("Delete"):
        try:
            # Modify the SQL query to delete the record with the specified EmployeeID
            sql = "DELETE FROM manager WHERE ManagerID = %s"
            val = (ManagerID,)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def main():
    st.title("Manager")
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
