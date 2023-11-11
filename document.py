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

def create_record():
    st.subheader("Create a Record")
    DocumentId = st.text_input("Enter DocumentId")
    DocumentName = st.text_input("Enter the DocumentName")
    uploadDate = st.date_input("Enter the UploadDate")
    Deadline = st.date_input("Enter the Deadline")
    EmployeeID = st.text_input("Enter the EmployeeID")

    if st.button("Create"):
        try:
            sql = "INSERT INTO document (DocumentId, DocumentName, uploadDate, Deadline, EmployeeID) VALUES (%s, %s, %s, %s, %s)"
            val = (DocumentId, DocumentName, uploadDate, Deadline, EmployeeID)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!!!")
        except mysql.connector.Error as err:
            if err.errno == 1062:
                st.error("Duplicate entry for DocumentId")
            else:
                st.error("An error occurred: {}".format(err))

def read_records():
    st.subheader("Read Records")
    mycursor.execute("SELECT * FROM document")
    result = mycursor.fetchall()
    if result:
        df = pd.DataFrame(result, columns=["DocumentID", "DocumentName", "UploadDate", "Deadline", "EmployeeID"])
        st.dataframe(df)
    else:
        st.write("No records found.")

def update_record():
    st.subheader("Update Record")
    DocumentId = st.text_input("Enter DocumentId to update")
    DocumentName = st.text_input("Enter new DocumentName")
    uploadDate = st.date_input("Enter new UploadDate")
    Deadline = st.date_input("Enter new Deadline")
    EmployeeID = st.text_input("Enter new EmployeeID")

    if st.button("Update"):
        try:
            sql = "UPDATE document SET DocumentName = %s, uploadDate = %s, Deadline = %s, EmployeeID = %s WHERE DocumentId = %s"
            val = (DocumentName, uploadDate, Deadline, EmployeeID, DocumentId)

            mycursor.execute(sql, val)
            mydb.commit()

            if mycursor.rowcount > 0:
                st.success(f"Record with DocumentId {DocumentId} updated successfully!")
            else:
                st.warning(f"No records updated. DocumentId {DocumentId} not found.")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def delete_record():
    st.subheader("Delete Record")
    DocumentId = st.text_input("Enter DocumentId to delete")

    if st.button("Delete"):
        try:
            sql = "DELETE FROM document WHERE DocumentId = %s"
            val = (DocumentId,)

            mycursor.execute(sql, val)
            mydb.commit()

            if mycursor.rowcount > 0:
                st.success(f"Record with DocumentId {DocumentId} deleted successfully!")
            else:
                st.warning(f"No records deleted. DocumentId {DocumentId} not found.")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def insert_document(p_DocumentId, p_DocumentName, p_uploadDate, p_Deadline, p_EmployeeID):
    try:
        mycursor.callproc('insert_document', (p_DocumentId, p_DocumentName, p_uploadDate, p_Deadline, p_EmployeeID))
        mydb.commit()
        st.success("Document inserted successfully!")
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")

def count_documents_by_employee(employee_id):
    try:
        mycursor.execute(f"SELECT count_documents_by_employee({employee_id})")
        result = mycursor.fetchone()[0]
        st.success(f"Number of documents for Employee ID {employee_id}: {result}")
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")

def main():
    st.title("Employee Management System")
    option = st.sidebar.selectbox("Select an operation", ("Document Management", "Insert Document", "Count Documents"))

    if option == "Document Management":
        option1 = st.sidebar.selectbox("Select an operation", ("Create", "Read", "Update", "Delete"))

        if option1 == "Create":
            create_record()
        elif option1 == "Read":
            read_records()
        elif option1 == "Update":
            update_record()
        elif option1 == "Delete":
            delete_record()

    elif option == "Insert Document":
        st.subheader("Insert Document")
        document_id = st.number_input("Document ID", min_value=1, step=1)
        document_name = st.text_input("Document Name")
        upload_date = st.date_input("Upload Date")
        deadline = st.date_input("Deadline")
        employee_id = st.number_input("Employee ID", min_value=1, step=1)

        if st.button("Insert Document"):
            insert_document(document_id, document_name, upload_date, deadline, employee_id)

    elif option == "Count Documents":
        st.subheader("Count Documents")
        employee_id = st.number_input("Enter Employee ID", min_value=1, step=1)

        if st.button("Count Documents"):
            count_documents_by_employee(employee_id)

if __name__ == "__main__":
    main()
