import tkinter as tk					
from tkinter import ttk,simpledialog
from datetime import date
import tkinter.filedialog as fd
import tkinter.messagebox as msg
import pandas as pd
from functools import partial
import json
import NameParser___Module as NModule
import NameAddressParser__Module as NaM
import Address_Parser__Module as AdM
import SingleNameParser_Module as NAD_API
import SingleAddressParser_Module as AD_API
import SingleNameAddressParser_Module as ADN_API

# Main Class for the name and address parsing, on individual level
class NameAddressParser:
    
    root = tk.Tk()
    tabControl = ttk.Notebook(root)
    tabControl.pack(expand = 1, fill ="both")

    
    
    #init function for creating th GUI as Tkinter
    def __init__(self, today = date.today()):
        NameAddressParser.root.title("Parser - US Census Bureau "+ str(today))
        NameAddressParser.root.geometry("1280x720")
        NameAddressParser.NameParser()
        NameAddressParser.AddressParser()
        NameAddressParser.NameAddressParser()
        NameAddressParser.root.mainloop()


    #Process for Name Parser, wherein after the click of the button "Choose Two Files" this method is triggered
 
    
    #Process for Address Parser, wherein after the click of the button "Choose Two Files" this method is triggered
     

    
    #Process for Address Parser, wherein after the click of the button "Choose Two Files" this method is triggered
     
    
    # This method is for creating a TAB in the GUI for Name Parser
    def NameParser():
        tab1 = ttk.Frame(NameAddressParser.tabControl)
        NameAddressParser.tabControl.add(tab1, text ='Name Parser')
        ttk.Label(tab1, 
          text ="Please Choose a Pipe Delimitted File").grid(column = 0, 
                               row = 0,
                               padx = 0,
                               pady = 0)  
        def Process_Name_Parser_input():
            msg.showinfo("Choose File","Select Input File")
            #Changed by salman

            df = fd.askopenfilenames( filetypes=[("TXT", ".txt"),("JSON",".json")]) 
            if df:
                Output=NModule.ExtractNames(df[0])
                if Output[0]:
                    msg.showinfo("Success",Output[1])
                else:
                    msg.showerror("Error!", Output[1])
            else: msg.showerror("Alert","Please select input file.")
            return
        
        def Process_Name_Parser():
            msg.showinfo("Choose File","Select Input File")
            #this file is used to give UI for the user to open a Input file
            df = fd.askopenfilenames( filetypes=[("TXT", ".txt")]) 
            if(df):
                msg.showinfo("Choose File","Select Truth File")
                #this file is used to give UI for the user to open a truth file
                truth = fd.askopenfilenames( filetypes=[("TXT", ".txt"),("JSON",".json")]) 
                
                
                
                if truth:
                    Output=NModule.ExtractNames(df[0],TruthSet=truth[0])
                    if Output[0]:
                        msg.showinfo("Success",Output[1])
                    else:
                        msg.showerror("Error!", Output[1])                
                    
                  
                    # except:
                    #     msg.showinfo("Alert!","File Reading Error !")
                else: msg.showerror("Alert!","Truth file is required!")
            else: msg.showerror("Alert","Please select input file.")
            return
                
                
                
                
                
                
                
                
                
                
                
                
               

        Nbutton = ttk.Button(tab1, text ="Choose Two Files (input and test)",width=30, command=Process_Name_Parser).grid(column = 5, 
                             row = 60,
                             padx = 10,
                             pady = 10)
        NbuttonSingle = ttk.Button(tab1, text ="Choose Single File (input)",width=30, command=Process_Name_Parser_input).grid(column = 5, 
                             row = 50,
                             padx = 10,
                             pady = 10)
        
        Or_Label=ttk.Label(tab1,text="Enter Name").grid(column = 4, 
                                 row = 10,
                                 padx = 10,
                                 pady = 10) 
        nad=tk.StringVar()
        single_input = ttk.Entry(tab1,width=100,textvariable=nad).grid(column = 5, 
                                 row = 10,
                                 padx = 10,
                                 pady = 10)
        ttk.Label(tab1, 
          text ="OR").grid(column = 5, 
                               row = 15,
                               padx = 0,
                               pady = 0) 

        
        
        def Single_Name(): 
            Convert=NAD_API.ExtractNames(nad.get())
            msg.showinfo("Output",Convert)
        
        ttk.Button(tab1, text ="Submit",width=20, command=Single_Name).grid(column =7, 
                                 row =10)    
                                      
                                              
    # This method is for creating a TAB in the GUI for Address Parser
    def AddressParser():
        tab2 = ttk.Frame(NameAddressParser.tabControl)
        NameAddressParser.tabControl.add(tab2, text ='Address Parser')
        ttk.Label(tab2, 
          text ="Please Choose a Pipe Delimitted File").grid(column = 0, 
                               row = 0,
                               padx = 5,
                               pady = 5)  
                                                             
        def Process_Address_Parser():
            msg.showinfo("Choose File","Select Input File")

            df = fd.askopenfilenames( filetypes=[("TXT", ".txt"),("JSON",".json")]) 
            if df:
                msg.showinfo("Choose File","Select Truth File")
                
                truth = fd.askopenfilenames( filetypes=[("TXT", ".txt")]) #this file is used to give UI for the user to open a file
                if truth:
                    Output=AdM.Address_Parser(df[0],TruthSet=truth[0])
                    if Output[0]:
                        msg.showinfo("Success",Output[1])
                    else:
                        msg.showerror("Error!", Output[1])                
                    
                  
                    # except:
                    #     msg.showinfo("Alert!","File Reading Error !")
                else: msg.showerror("Alert!","Truth file is required!")
            else: msg.showerror("Alert","Please select input file.")
            return
        
        
        def Process_Address_Parser_input():
            msg.showinfo("Choose File","Select Input File")

            df = fd.askopenfilenames( filetypes=[("TXT", ".txt"),("JSON",".json")]) 
            if df:
                Output=AdM.Address_Parser(df[0])
                if Output[0]:
                    msg.showinfo("Success",Output[1])
                else:
                    msg.showerror("Error!", Output[1])
            else: msg.showerror("Alert","Please select input file.")
            return
        
        
        Nbutton = ttk.Button(tab2, text ="Choose Two Files (input and test)",width=30, command=Process_Address_Parser).grid(column = 5, 
                             row = 60,
                             padx = 10,
                             pady = 10)
        NbuttonSingle = ttk.Button(tab2, text ="Choose Single File (input)",width=30, command=Process_Address_Parser_input).grid(column = 5, 
                             row = 50,
                             padx = 10,
                             pady = 10)
        
        Or_Label=ttk.Label(tab2,text="Enter Address").grid(column = 4, 
                                 row = 10,
                                 padx = 10,
                                 pady = 10) 
        
        nad=tk.StringVar()
        single_input = ttk.Entry(tab2,width=100,textvariable=nad).grid(column = 5, 
                                 row = 10,
                                 padx = 10,
                                 pady = 10) 
        ttk.Label(tab2, 
          text ="OR").grid(column = 5, 
                               row = 15,
                               padx = 0,
                               pady = 0) 
        # text = tk.Text(tab2, height=24)
        # text.grid(row=55, column=5, sticky=tk.EW)
        
        # # create a scrollbar widget and set its command to the text widget
        # scrollbar = tk.Scrollbar(tab2, orient='vertical', command=text.yview)
        # scrollbar.grid(column=6, row=55, rowspan=2,  sticky="ns")
        
        # #  communicate back to the scrollbar
        # text['yscrollcommand'] = scrollbar.set
        
        
        # text_result = tk.Text(tab2, height=5,width=30)
        # text_result.grid(row=55, column=7,padx=20,pady=20)
        
        import textwrap


        def wrap(string, lenght=60):
            return '\n'.join(textwrap.wrap(string, lenght))
        
        
        tree = ttk.Treeview(tab2, column=["Address Component","Address Token","Mask Token","Exception","File"] ,selectmode="extended",show='headings',height=10)
        for item in tree.get_children():
            tree.delete(item)
        tree.column("# 1", width=50, stretch='YES')
        tree.heading("# 1", text="Address Component")
        
        tree.column("# 2", width=200, stretch='YES')
        tree.heading("# 2", text="Address Token")
        
        tree.column("# 3", width=200, stretch='YES')
        tree.heading("# 3", text="Mask Token")
        
        tree.column("# 4", width=50, stretch='YES')
        tree.heading("# 4", text="Exception")
        
        tree.column("# 5", width=200, stretch='YES')
        tree.heading("# 5", text="File Name")
        
        
        def Single_Address():
            
            def submit():
                # Get the checkbox state
                checkbox_state = checkbox_var.get()
                txtMask_1 = tk.StringVar()
                txtFirstPhaseList = tk.StringVar()
                txtInitials = tk.StringVar()
                Mask_1 = txtMask_1.get()
                FirstPhaseList = txtFirstPhaseList.get()
                initials = txtInitials.get()
                # Print the checkbox state
                if checkbox_var.get():
                    # AD_API.Address_Parser()
                    print("Forced Exception Clicked")

                else:
                    print("Not a Forced Exception")
            checkbox_var = tk.IntVar()

            # Create the checkbox
            checkbox = ttk.Checkbutton(tab2, text="Forced Exception", variable=checkbox_var)
            checkbox.grid(row=12, column=5, padx=10, pady=10)

            # Create the submit button
            submit_button = ttk.Button(tab2, text="Forced Exception", command=submit)
            submit_button.grid(row=13, column=5, padx=10, pady=10)
            # toggle_state = tk.StringVar(value="No")


            # Create the form elements with custom styling
            # Forced_Except_Label = ttk.Label(tab2, text="Forced Exception? ", font=("Arial", 12))
            # Forced_Except_Label.grid(row=5, column=0, sticky=tk.W, pady=5)
            # toggle_button = ttk.Checkbutton(tab2, onvalue="Yes", offvalue="No", variable=toggle_state, style="Toggle.TCheckbutton")

            # toggle_button.grid(row=5, column=0,columnspan=2, pady=5)
            # style.configure("Toggle.TCheckbutton", font=("Arial", 14))
            
            
            s = ttk.Style()
            s.configure('Treeview', rowheight=35, background="black", 
                fieldbackground="black", foreground="white")
            
            
            initial = simpledialog.askstring("Optional", "Your Initials")
           
            Convert=AD_API.Address_Parser(nad.get(),initial)
            
            Result=Convert[0]
            
            try:  
                
                for item in tree.get_children():
                    tree.delete(item)
                tree.insert('','end',values=(wrap('Mask'),wrap(Convert[1]),"","",""))
                for k, v in Result["Output"].items():  
                    tree.insert('', 'end', values=(wrap(k),wrap(v[1]),wrap(v[0])))
                
            except:
               
                for item in tree.get_children():
                    tree.delete(item)
                tree.insert('','end',values=("","",Convert[1],Convert[2]))


            
            
            
            tree.grid(row=55, column=5, sticky=tk.EW)
            
            
        
        ttk.Button(tab2, text ="Submit",width=30, command=Single_Address).grid(column = 7, 
                                 row = 10)    

        return



    def NameAddressParser():
        
        tab3 = ttk.Frame(NameAddressParser.tabControl)
        NameAddressParser.tabControl.add(tab3, text ='Name and Address Parser')
        ttk.Label(tab3, 
          text ="Please Choose a Pipe Delimitted File").grid(column = 0, 
                               row = 0,
                               padx = 5,
                               pady = 5)  
        def Process_Name_Address_Parser():
            msg.showinfo("Select File","Please select the input file")
            df = fd.askopenfilenames( filetypes=[("TXT", ".txt")]) #this file is used to give UI for the user to open a file
            if df:
                # msg.showinfo("Select File","Please select the input file")
                # truth = fd.askopenfilenames( filetypes=[("TXT", ".txt")])
                # if truth:
                ReturnVal=NaM.NameandAddressParser(df[0])
                jsonData = json.dumps(ReturnVal[0], indent=2)
                with open('OutputNameAddressParsedFile.txt', 'w') as out_file:
                    json.dump(jsonData, out_file, sort_keys = True, indent = 4,ensure_ascii = False)
                    msg.showinfo("Success!","Parsing is Successful, Output File Name 'OutputNameAddressParsedFile' is Generated!")         
                # text = tk.Text(tab3, height=28)
                # text.grid(row=80, column=10, sticky=tk.EW)
                
                # # create a scrollbar widget and set its command to the text widget
                # scrollbar = ttk.Scrollbar(tab3, orient='vertical', command=text.yview)
                # scrollbar.grid(row=80, column=11, sticky=tk.NS)
                
                # #  communicate back to the scrollbar
                # text['yscrollcommand'] = scrollbar.set

                # text.insert('end', jsonData)
                
                
                # text1 = tk.Text(tab3, height=5)
                # text1.grid(row=10, column=30, sticky=tk.NW)
                
                # create a scrollbar widget and set its command to the text widget
                
                #  communicate back to the scrollbar
                String="Percentage of Parsed Name and Address"
                String+="= "+str(round(ReturnVal[1],2))
                String+="\n% of Correctly parsed Addresses= "+str(round(ReturnVal[1],2))
                text.delete("1.0",'end-1c')
                text_result.delete("1.0",'end-1c')
            
                text.insert('end', jsonData)
                text_result.insert('end', String)
            # else: msg.showerror("Warning","Truth file is required.")
            else: msg.showerror("Warning","Input file is not selected.")

            return
        Or_Label=ttk.Label(tab3,text="Enter Name And Address").grid(column = 4, 
                                 row = 10,
                                 padx = 10,
                                 pady = 10) 
        Nbutton = ttk.Button(tab3, text ="Choose Two Files",width=30, command= Process_Name_Address_Parser).grid(column = 5, 
                             row = 50,
                             padx = 10,
                             pady = 10)
        nad=tk.StringVar()
        single_input = ttk.Entry(tab3,width=100,textvariable=nad).grid(column = 5, 
                                 row = 10,
                                 padx = 10,
                                 pady = 10)
        ttk.Label(tab3, 
          text ="OR").grid(column = 5, 
                               row = 15,
                               padx = 0,
                               pady = 0) 
        text = tk.Text(tab3, height=24)
        text.grid(row=55, column=5, sticky=tk.EW)
        
        # create a scrollbar widget and set its command to the text widget
        scrollbar = tk.Scrollbar(tab3, orient='vertical', command=text.yview)
        scrollbar.grid(column=6, row=55, rowspan=2,  sticky="ns")
        
        #  communicate back to the scrollbar
        text['yscrollcommand'] = scrollbar.set
        
        
        text_result = tk.Text(tab3, height=5,width=30)
        text_result.grid(row=55, column=7,padx=20,pady=20)
        
        def Single_Name_Address(): 
            Convert=ADN_API.NameandAddressParser(nad.get())
            msg.showinfo("Output",Convert)
        
        ttk.Button(tab3, text ="Submit",width=30, command=Single_Name_Address).grid(column = 7, 
                                 row = 10)
        return
name=NameAddressParser()