from tkinter import Tk
from docxtpl import DocxTemplate
from tkinter import *
from datetime import datetime
class Window():
    def __init__(self,tkinter:Tk):
        self.app = tkinter
        self.app.title("Word File Processor")
        self.app.geometry("400x400")


        self.welcome_frame = Frame(self.app)
        self.welcome_frame.pack()

        welcome_lbl = Label(self.welcome_frame, text="Welcome to the Word File Processor")
        welcome_lbl.grid(row=0,column=1)

        #Creating a new frame for input boxes and labels
        self.action_frame = Frame(self.app)
        self.action_frame.pack()

        recruiter_name_lbl = Label(self.action_frame, text="Recruiter's Name: ")
        recruiter_name_lbl.grid(row=0,column=0)

        self.recruiter_name_entry = Entry(self.action_frame, width="25")
        self.recruiter_name_entry.grid(row=0, column=1)

        recruiter_job_lbl = Label(self.action_frame, text="Recruiter's Job Title: ")
        recruiter_job_lbl.grid(row=1, column=0)

        self.recruiter_job_entry = Entry(self.action_frame, width="25")
        self.recruiter_job_entry.grid(row=1, column=1)

        company_name_lbl = Label(self.action_frame, text="Company's Name: ")
        company_name_lbl.grid(row=2, column=0)

        self.company_name_entry = Entry(self.action_frame, width="25")
        self.company_name_entry.grid(row=2, column=1)

        company_address_lbl = Label(self.action_frame, text="Company's Address: ")
        company_address_lbl.grid(row=3, column=0)

        self.company_address_entry = Entry(self.action_frame, width="25")
        self.company_address_entry.grid(row=3, column=1)

        company_city_lbl = Label(self.action_frame, text="Company's City: ")
        company_city_lbl.grid(row=4, column=0)

        self.company_city_entry = Entry(self.action_frame, width="25")
        self.company_city_entry.grid(row=4, column=1)

        self.selected_state = StringVar(value="MA")
        states = self.getStates()
        drowpdown_option = OptionMenu(self.action_frame, self.selected_state, *states.values())
        drowpdown_option.grid(row=5, column=1)


        company_state_lbl = Label(self.action_frame, text="Company's State: ")
        company_state_lbl.grid(row=5, column=0)

        #self.company_state_entry = Entry(self.action_frame, width="25")
        #self.company_state_entry.grid(row=5, column=1)

        company_zip_lbl = Label(self.action_frame, text="Company's Zip Code: ")
        company_zip_lbl.grid(row=6, column=0)

        self.company_zip_entry = Entry(self.action_frame, width="25")
        self.company_zip_entry.grid(row=6, column=1)

        job_title_lbl = Label(self.action_frame, text="Job title: ")
        job_title_lbl.grid(row=7, column=0)

        self.job_title_entry = Entry(self.action_frame, width="25")
        self.job_title_entry.grid(row=7, column=1)

        job_type_lbl = Label(self.action_frame, text="Job Type: ")
        job_type_lbl.grid(row=8, column=0)

        #self.job_type_entry = Entry(self.action_frame, width="25")
        #self.job_type_entry.grid(row=8, column=1)
        options = ["internship","full-time job","part-time job", "contract"]
        self.select_value = StringVar(value="internship")
        drowpdown_option = OptionMenu(self.action_frame,self.select_value, *options)
        drowpdown_option.grid(row=8, column=1)

        website_name_lbl = Label(self.action_frame, text="Website Name: ")
        website_name_lbl.grid(row=9, column=0)

        self.website_name_entry = Entry(self.action_frame, width="25")
        self.website_name_entry.grid(row=9, column=1)

        register_frame = Frame(self.app)
        register_frame.pack()

        self.register_btn = Button(register_frame,text="Register",command=self.run ,width=20)
        self.register_btn.grid(row=0,column=0,pady=20)


    def run(self):
        self.document = DocxTemplate("original.docx")
        self.date = datetime.today().strftime("%b %d, %Y")
        self.recruiterName = self.recruiter_name_entry.get()
        self.recruiterJobTitle = self.recruiter_job_entry.get()
        self.name = self.company_name_entry.get()
        self.address = self.company_address_entry.get()
        self.city = self.company_city_entry.get()
        self.state = self.selected_state.get()

        self.zip_code = self.company_zip_entry.get()
        job_type =  self.select_value.get()

        self.job_title = self.job_title_entry.get()
        self.website = self.website_name_entry.get()
        self.job_type_address = self.adderssing_job_type(job_type)
        data =  {"date":self.date,
                "recruiter_name":self.recruiterName.title(),
                "recruiter_job_title":self.recruiterJobTitle.capitalize(),
                "company_name": self.name.capitalize(),
                "website_name": self.website.capitalize(),
               "company_zipcode":self.zip_code,
                "company_city": self.city.capitalize(),
               "company_address": self.address ,
                 "job_type_address": self.job_type_address,
               "company_state":self.state,
               "job_type":job_type,
               "job_title": self.job_title.capitalize()}
        if self.recruiterName.strip()=="" or self.recruiterJobTitle.strip()=="" or self.website.strip()=="" or self.job_title.strip()=="" or self.name.strip()=="" or self.address.strip()=="" or self.city.strip()=="" or self.zip_code.strip()=="":
            print("Nope")
        else:
            self.document.render(data)
            self.document.save("generated.docx")
            print(self.recruiterName)
        self.app.mainloop()
    def getStates(self):
        us_states = {
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virginia': 'VA',
            'Washington': 'WA',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY'
        }
        return us_states

    def adderssing_job_type(self,job_type):
        vowels = ['a','e','i','o','u']
        if job_type[0] in vowels:
            return "an intern"
        else:
            if job_type == "part-time job":
                return "a part-timer"
            elif job_type == "full-time job":
                return 'a full-timer'
            else:
                return "a contractor"