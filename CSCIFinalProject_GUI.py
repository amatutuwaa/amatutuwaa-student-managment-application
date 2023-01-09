import tkinter as tk 
import webbrowser
import pandas as pd
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut 
from geopy.geocoders import Nominatim
from tkinter import font


class FullWindow:
    def __init__ (self):
        self.window = tk.Tk()
        self.window.configure (bg= 'white')
        self.old_job_listings = []

    def create_header_frame(self): 
        header_frame = tk.Frame(master=self.window, bg="white")
        header_frame.pack()
        self.create_header_sub_frames(header_frame)

    def create_header_sub_frames(self, header_frame):
        frame_a = tk.Frame(master=header_frame, width=500, height=100, bg="white")
        frame_a.pack(fill=tk.Y, side=tk.LEFT)

        frame_b = tk.Frame(master=header_frame, width=500, height = 100, bg="white")
        frame_b.pack(fill=tk.Y, side=tk.LEFT)

        label_a = tk.Label(master=frame_a, text="THE STUDENT MANAGEMENT APP", bg = "white", anchor = "w", font = self.firstfont )
        label_a.grid(row = 0, column = 0,sticky = "nsew", padx = (0, 110), pady = 0)

        label_b = tk.Label(master=frame_a, text="CLARK UNIVERSITY", bg = "white", anchor = "w", font = self.secondfont)
        label_b.grid(row = 1, column = 0, sticky = "nsew",  padx = (0, 110), pady = 0)

        label_c = tk.Label(master=frame_b, text=" ", bg = "white")
        label_c.grid(row = 0, column = 0, sticky = "ew", padx = 10, pady = 17)

        label_c = tk.Label(master=frame_b, text=" ", bg = "white")
        label_c.grid(row = 0, column = 0, sticky = "ew", padx = 10, pady = 0)


        label_c = tk.Label(master=frame_b, text="Student Schedule", bg = "white", font = self.thirdfont)
        label_c.grid(row = 1, column = 0, sticky = "ns", padx = 10, pady = 0)

        label_d = tk.Label(master=frame_b, text="The Grade Calculator", bg = "white", font = self.thirdfont)
        label_d.grid(row = 1, column = 1, sticky = "ns", padx = 10, pady = 0)

        label_e = tk.Label(master=frame_b, text="Find Internships and Jobs", bg = "white", font = self.thirdfont)
        label_e.grid(row = 1, column = 2, sticky = "ns", padx = 10, pady = 0)

        frame_a.pack()
        frame_b.pack()



    def create_banner_frame(self):
        frame_c = tk.Frame(master=self.window, width=1000, height = 300, bg= "red4")
        frame_c.pack(fill=tk.BOTH)

        label_f = tk.Label(master= frame_c, text = " ", bg = "red4", fg= "white", font = self.spacefont)
        label_f.pack()

        label_f = tk.Label(master= frame_c, text = "W E L C O M E  T O", bg = "red4", fg= "white", font = self.sixthfont)
        label_f.pack()

        label_f = tk.Label(master= frame_c, text = " ", bg = "red4", fg= "white", font = self.spacefont)
        label_f.pack()

        label_f = tk.Label(master= frame_c, text = "T H E", bg = "red4", fg= "white", font = self.forthfont)
        label_f.pack()

        label_f = tk.Label(master= frame_c, text = "S T U D E N T  M A N A G E M E N T", bg = "red4", fg= "white", font = self.fifthfont)
        label_f.pack( padx = 167, pady = 0)

        label_f = tk.Label(master= frame_c, text = "A P P", bg = "red4", fg= "white", font = self.forthfont)
        label_f.pack( padx = 300, pady = 0)

        label_f = tk.Label(master= frame_c, text = " ", bg = "red4", fg= "white", font = self.spacefont)
        label_f.pack()

        label_f = tk.Label(master= frame_c, text = "C L A R K  U N I V E R S I T Y", bg = "red4", fg= "white", font = self.secondfont)
        label_f.pack( padx = 300, pady = 0)

        label_f = tk.Label(master= frame_c, text = " ", bg = "red4", fg= "white", font = self.spacefont)
        label_f.pack()

        label_f = tk.Label(master= frame_c, text = "C S C I  1 2 0  F I N A L  P R O J E C T", bg = "red4", fg= "white", font = self.eigthfont)
        label_f.pack( padx = 300, pady = 0)

        label_f = tk.Label(master= frame_c, text = "By Ama Tutuwaa Osei-Akoto", bg = "red4", fg= "white", font = self.eigthfont)
        label_f.pack( side=tk.RIGHT, padx = 30, pady = 0)

        frame_c.pack()


    def create_footer_frames(self):
        footer_frame = tk.Frame(master=self.window, bg="white")
        footer_frame.pack()
        self.create_contact_frame(footer_frame)
        self.create_form_frame(footer_frame)

    def open_link_in_browser (self, link):
        webbrowser.open(link , new=2)


    # Frame + Labels for Left hand side of red belt
    def create_contact_frame(self, footer_frame):
        frame_d = tk.Frame(master=footer_frame, width=500, height = 100, bg="white")
        frame_d.pack(fill=tk.Y, side=tk.LEFT)

        label_g = tk.Label(master=frame_d, text= "C L A R K  U N I V E R S I T Y", bg = "white", anchor = "w", font = self.seventhfont )
        label_g.pack(fill=tk.X, padx = (400, 50), pady = 0)

        label_g = tk.Label(master=frame_d, text= "CHALLENGE CONVENTION || CHANGE OUR WORLD", bg = "white", anchor = "w", font = self.eigthfont )
        label_g.pack(fill=tk.X, padx = (400, 50), pady = 0)

        label_g = tk.Label(master= frame_d, text = " ___                                                                              ", bg = "white", fg= "black", font= self.sixthfont)
        label_g.pack(fill=tk.X, padx = (400, 50), pady = 0)

        label_g = tk.Label(master= frame_d, text = " ", bg = "white", fg= "white", font = self.spacefont)
        label_g.pack()

        label_g = tk.Label(master=frame_d, text= "C O N T A C T", bg = "white", anchor = "w", font = self.ninthfont )
        label_g.pack(fill=tk.BOTH, padx = (400, 50), pady = 0)

        label_g = tk.Label(master=frame_d, text= "5 0 8 - 7 9 3 - 7 7 1 1", bg = "white", anchor = "w", font = self.eigthfont )
        label_g.pack(fill=tk.BOTH, padx = (400, 50), pady = 0)

        label_g = tk.Label(master= frame_d, text = " ", bg = "white", fg= "white", font = self.spacefont)
        label_g.pack()

        label_g = tk.Label(master=frame_d, text= "9 5 0  M a i n  S t r e e t  W o r c e s t e r ,  M A  0 1 6 1 0", bg = "white", anchor = "w", font = self.eigthfont )
        label_g.pack(fill=tk.BOTH, padx = (400, 50), pady = 0)

        label_g = tk.Label(master= frame_d, text = " ", bg = "white", fg= "white", font = self.spacefont)
        label_g.pack()

        # Creating Facebook Button
        self.photo1 = tk.PhotoImage(file = r"./facebookicon.png")
        self.photoimage1 = self.photo1.subsample(3, 3) 

        facebook_button = tk.Button(master = frame_d, image = self.photoimage1, bg="white", fg="black", command = lambda: self.open_link_in_browser('https://www.facebook.com/89555183497/'))
        facebook_button.pack(side=tk.LEFT, padx = (400, 0), pady = 0)

        # Creating Twitter Button
        self.photo2 = tk.PhotoImage(file = r"./twittericon.png")
        self.photoimage2 = self.photo2.subsample(3, 3)

        twitter_button = tk.Button(master = frame_d, image = self.photoimage2, bg="white", fg="black", command = lambda: self.open_link_in_browser('https://twitter.com/clarkuniversity?s=21'))
        twitter_button.pack(side=tk.LEFT, padx = 2, pady = 0)

        # Creating Instagram Button
        self.photo3 = tk.PhotoImage(file = r"./instaicon.png")
        self.photoimage3 = self.photo3.subsample(3, 3)

        instagram_button = tk.Button(master = frame_d, image = self.photoimage3, bg="white", fg="black", command = lambda: self.open_link_in_browser('https://instagram.com/clarkuniversity?igshid=kzv0ilvg8ws7'))
        instagram_button.pack(side=tk.LEFT, padx = 2, pady = 0)

        # Creating Youtube Button
        self.photo4 = tk.PhotoImage(file = r"./youtubeicon.png")
        self.photoimage4 = self.photo4.subsample(3, 3)

        youtube_button = tk.Button(master = frame_d, image = self.photoimage4, bg="white", fg="black", command = lambda: self.open_link_in_browser('https://www.youtube.com/c/clarkuniversity'))
        youtube_button.pack(side=tk.LEFT, padx = 2 , pady = 0)

        frame_d.pack()


    def create_form_frame(self, footer_frame):
        frame_e = tk.Frame(master=footer_frame, width=500, height=100, bg="white")
        frame_e.pack(fill=tk.Y, side=tk.LEFT)

        label_g = tk.Label(master=frame_e, text= " S E A R C H   F O R  J O B S  A N D  I N T E R N S H I P S   L I S T I N G S", bg = "white", anchor = "w", font = self.ninthfont )
        label_g.pack(fill=tk.X, padx = (107, 300), pady = 0)
        
        label = tk.Label(master=frame_e, text="Enter Your Name:", bg= 'white', fg = 'red4')
        label.pack(padx = (50, 300) , pady = 0)
        entry = tk.Entry(master = frame_e, width = 50)
        entry.pack(padx = (50, 300) , pady = 0)


        label = tk.Label(master=frame_e, text="Enter Your Email:", bg= 'white', fg = 'red4')
        label.pack(padx = (50, 300) , pady = 0)
        entry = tk.Entry(master = frame_e,  width = 50)
        entry.pack(padx = (50, 300) , pady = 0)

        label = tk.Label(master = frame_e, text= "Enter Your current City", bg = 'white', fg = 'red4')
        label.pack(padx = (50, 300) , pady = 0)
        label = tk.Label(master=frame_e, text="Unfortunately Currently the Job Listing application is limited to \n the State of Massachusetts so kindly choose a city located within Massachusetts:", bg= 'white', fg = 'black', font = self.tenthfont)
        label.pack(padx = (50, 300) , pady = 0)

        Massachusetts_cities = self.get_cities()

        mass_variable = tk.StringVar(self.window)
        mass_variable.set(Massachusetts_cities[0]) 

        opt = tk.OptionMenu(frame_e, mass_variable, *Massachusetts_cities)
        opt.config(width=60, font=('Avenir Next', 12))
        opt.pack(padx = (50, 300) , pady = 0)

        # Creating Career Fields Drop Down Menu
        label = tk.Label(master = frame_e, text= "Choose a Career Field of Interest from the Drop-down Menu below:", bg = 'white', fg = 'red4')
        label.pack(padx = (50, 300) , pady = 0)

        Career_Fields = [ 'Architecture and Engineering' , 'Arts, Culture and Entertainment' , 'Business Management and Administration' , 
        'Communications' , 'Community and Social Services' , 'Education' , 'Science and Technology' , 'Government' , 'Environment, Fishing, Forestry' , 'Health and Medicine' , '' ]

        variable = tk.StringVar(self.window)
        variable.set(Career_Fields[0]) 

        opt = tk.OptionMenu(frame_e, variable, *Career_Fields)
        opt.config(width=60, font=('Avenir Next', 12))
        opt.pack(padx = (50, 300) , pady = 0)

        label_g = tk.Label(master= frame_e, text = " ", bg = "white", fg= "white", font = self.spacefont)
        label_g.pack()

        # Creating "Submit" Button

        submit_button = tk.Button(master = frame_e, text="Submit", bg="white", fg="black", command = lambda: self.find_job_listings(mass_variable, variable))
        submit_button.pack(side=tk.RIGHT, padx = (50, 300), pady = 0)

    # Reading Massachusetts cities from the Massachusetts_cities.txt file

    def get_cities(self):
        Massachusetts_cities = []
        file = open ('Massachusetts_cities.txt')
        for line in file:
            if "(" not in line:
                Massachusetts_cities.append(line[0:-1])
        return Massachusetts_cities


    def create_job_listings_result_frame(self):

        self.frame_f =tk.Frame(master=self.window, width=1000, height = 300, bg= "white")
        self.frame_f.pack(fill=tk.BOTH)
        self.frame_f.pack_forget()

        label_h = tk.Label(master=self.frame_f, text="J O B S   A N D   I N T E R N S H I P   F I N D E R   R E S U L T S", bg = "white", fg ="red4" , anchor = "w", font = self.secondfont)
        label_h.pack(pady = 0)

    def create_fonts(self): 
        self.firstfont= font.Font(family ='Avenir Next', size = 40, weight = 'bold')
        self.secondfont = font.Font(family = 'Avenir Next', size = 25)
        self.thirdfont = font.Font (family = 'Avenir Next', size = 15)
        self.forthfont = font.Font (family = 'Avenir Next', size = 15)
        self.fifthfont = font.Font (family = 'Avenir Next', size = 68)
        self.sixthfont = font.Font (family = 'Avenir Next Condensed' , size = 20)
        self.seventhfont = font.Font (family = 'Avenir Next', size = 20, weight = 'bold')
        self.spacefont = font.Font (family = 'Avenir Next', size = 12)
        self.eigthfont = font.Font (family = 'Avenir Next' , size = 13)
        self.ninthfont = font.Font (family = 'Avenir Next' , size = 13, weight = 'bold')
        self.tenthfont = font.Font (family = 'Avenir Next' , size = 8)
 

    def compute_distance(self, source, destination):

        source_coordinates = self.findGeocode (source)
        destination_coordinates = self.findGeocode (destination)
        if source_coordinates == None or destination_coordinates == None:
            return 100 
        else:    
            source_coordinates = (source_coordinates.latitude , source_coordinates.longitude)
            destination_coordinates = (destination_coordinates.latitude , destination_coordinates.longitude)
            return geodesic(source_coordinates, destination_coordinates).km

    # Code Inspiration from https://www.geeksforgeeks.org/how-to-find-longitude-and-latitude-for-a-list-of-regions-or-country-using-python/

    def findGeocode(self, city): 
        return None     
        try: 
            
            geolocator = Nominatim(user_agent="app") 
            
            return geolocator.geocode(city) 
        
        except GeocoderTimedOut: 
            
            return self.findGeocode(city)

    def find_job_listings(self, selected_massachusetts_city, selected_career_feild):
        jobs  = pd.read_csv("JOB Listings.csv")
        
        matching_jobs = jobs [jobs['CAREER FIELDS'] == selected_career_feild.get()] 

        source = selected_massachusetts_city.get()
        matching_jobs['DISTANCE'] = matching_jobs['LOCATION'].map(lambda destination:self.compute_distance(source, destination))

        sorted_matched_jobs = matching_jobs.sort_values(by=['DISTANCE'])
        print (sorted_matched_jobs)

        for frame in self.old_job_listings:
            frame.destroy()

        for index, row in sorted_matched_jobs.iterrows():
        
            frame_g =tk.Frame(master=self.frame_f, width=1000, height = 300, bg= "white", highlightbackground = "red4", highlightthickness = "1")
            frame_g.pack(fill=tk.BOTH, pady = "5")

            label_i = tk.Label(master= frame_g, text = row["ROLE"], bg = "white", fg= "red4", font = self.spacefont, anchor = "w", width = 50)
            label_i.grid(row = 0, column = 0, padx = (545, 50), pady = 0, sticky = "ew")

            label_i = tk.Label(master= frame_g, text = row["COMPANY"], bg = "white", fg= "red4", font = self.spacefont, anchor = "w", width = 50)
            label_i.grid(row = 1, column = 0, padx = (545, 50), pady = 0, sticky = "ew")

            label_i = tk.Label(master= frame_g, text = row["LOCATION"], bg = "white", fg= "red4", font = self.spacefont, anchor = "e", width = 50)
            label_i.grid(row = 0, column = 1, pady = 0, sticky = "ew")

            label_i = tk.Button(master= frame_g, text = "Click Here to Apply", bg = "white", fg= "red4", font = self.spacefont, command = lambda:self.open_link_in_browser(row["LINK"]), width = 13)
            label_i.grid(row = 1, column = 1, padx = (50, 0), pady = 0, sticky = "E")

            self.old_job_listings.append(frame_g)

        self.frame_f.pack(fill=tk.BOTH)

# Driver Function

    def run (self):
        self.create_fonts()
        self.create_header_frame()
        self.create_banner_frame()
        self.create_footer_frames()
        self.create_job_listings_result_frame()
        self.window.mainloop()
    

if __name__ == '__main__':
    Class = FullWindow()
    Class.run()
    