import tkinter as tk
from tkinter import filedialog
import os

class ImageToPDFConverter :
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()
        self.selected_images_listbox =tk.Listbox(root,selectmode=tk.MULTIPLE)
        #self.selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE) 
        
        self.initialize_ui()  
        
    def initialize_ui(self):
        title_label = tk.Label(self.root, text="IMAGE TO PDF CONVERTER",
                               font=("Helvetica",16,"bold"))
        title_label.pack(pady=10)
        
        select_images_button = tk.Button(self.root, text="Select Images",command=self.select_images)
        select_images_button.pack(pady=(0,10))
        
        self.selected_images_listbox.pack(pady=(0,10),fill=tk.BOTH,expand=True)
        
        label = tk.Label(self.root,text="Enter output PDF name:")
        label.pack()
        
        pdf_name_entry =tk.Entry(self.root, textvarible =self.output_pdf_name, width =40, justify='center')
        pdf_name_entry.pack()
        
        converter_button = tk.Button(self.root, text="Converter to PDF", command=self.converter_images_to_pdf)
        converter_button.pack(pady=(20,40))
        
    def select_images(self):
        self.image_paths = filedialog.askopenfilenames(title="Select Images",filetypes=
                                                       [("image file;","*.png;*.jpg;*.jpeg")])
        self.update_selected_images_listbox()
        
    def update_selected_images_listbox(self):
        self.selected_images_listbox.delete(0,tk.END)
        
        for iamge_path in self.image_paths:
            _, image_path = os.path.split(image_path)
            self.selected_images_listbox.insert(tk.END, image_path)
            
    def convert_images_to_pdf(self):
        if not self.image_paths:
            return
        
def main():
    root = tk.Tk()
    root.title("Image to PDF")
    coverter = ImageToPDFConverter(root)
    root.geometry("400x600")
    root.mainloop()
    
if __name__ == "__main__":
    main()