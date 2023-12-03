import streamlit as st
import pandas as pd
import subprocess

def main():

    #Priority and Time Needed (divided by 6)
    predefined_data = {
        'Surgery/Operation' : [1, 10],
        'Consultation' : [2, 5],
        'Tests' : [3, 7], 
        'Vaccination' : [4, 2], 
        'Checkup': [5, 4]
    }
    
    #Table Contents
    table_header = ['Appointment Time', 'Appointment Name', 'Priority', 'Time Needed (mins)']
    table_data = []
    
    
    #Headings
    st.markdown("<h1 style='text-align: center; color: #6e9da0'>Good Life Hospital</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #757575'>Appointments Site</h4>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center;'>Enter the Details</h2>", unsafe_allow_html=True)
    
    
    #Input Form
    name = st.text_input('Your Name')
    arrival_time = st.text_input('Time you are available for appointment (0 - 9)')
    
    type = st.selectbox('What is the appointment for', ('Surgery/Operation', 'Consultation', 'Tests', 'Vaccination', 'Checkup'))
    
    
    st.write("")
    with st.columns(3)[1]:
        button = st.button('Enter', use_container_width=True)
        st.write("")    
        
    priority, time_needed = predefined_data[type]
    
    if button:
        
        if arrival_time and name:        
            data = "{0} {1}-{2} {3} {4}".format(arrival_time, name, type, priority, time_needed)
            
            with open('./data.txt', 'a') as file:
                file.write(data) 
                file.write("\n")   
              
        else:
            st.error("Fill all the Fields")        
        
    st.write("")
    
    with open('./data.txt', 'r') as file:
        content = file.read()
    
    #Displaying the Appointment Details
    if content:
    
        btn, _, _, _ = st.columns(4)    
            
        #Reset Button    
        with btn:      
            
            x = st.button('Reset Appointments', use_container_width=True)
            if x:
                
                with open('./data.txt', 'w') as file:
                    file.write("")    
                    
                with open('./output.txt', 'w') as file:
                    file.write("")        
        
        if btn and x:
            st.info('Click again for removing the table')
        
            
        #Display the data in a Table
        with open('./data.txt', 'r') as file:
            data = file.read()
            
        if data:
            data = data.split("\n")
            
            for i in data[:-1]:
                table_data.append(i.split(' '))
                
        dataframe = pd.DataFrame(table_data, columns = table_header)
        
        st.table(dataframe)
        
        #Download Button
        _, _, _, download = st.columns(4)
        
        with download:    
            csv_file = dataframe.to_csv(index=False)
            st.download_button("Download as CSV", csv_file, file_name="table_data.csv", key="download_csv_button", use_container_width=True)  
                                        
        
        #Running the Scheduling Code
        order_of_scheduling = None 
        with st.columns(3)[1]:
            if st.button('Execute', use_container_width=True):
                
                with open('./output.txt', 'w') as file:
                    file.write("")   
                
                python_file_path = './sceduling.py'
                subprocess.run(["python", python_file_path])
                
                with open('./output.txt', 'r') as file:
                    order_of_scheduling = file.readlines()
        
        st.write("")   
        
        if order_of_scheduling != None:                
            for i in order_of_scheduling:
                st.write(i, use_container_width=True)   
                
                
        with open('./data.txt', 'r') as file:
            content = file.read() 
    
if __name__ == "__main__":   
        
    main()
    