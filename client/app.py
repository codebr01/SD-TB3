import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg;*.png;*.jpeg")])
    if not file_path:
        return
    try:
        with open(file_path, "rb") as img_file:
            files = {"file": img_file}
            response = requests.post("http://127.0.0.1:8000/upload/", files=files)
            if response.status_code == 200:
                data = response.json()
                messagebox.showinfo("Sucesso", f"Imagem enviada!\nID: {data['id']}\nCaminho Original: {data['original']}\nCaminho Processado: {data['processed']}")
                
                print(data)

                display_images(data['id'])
            else:
                messagebox.showerror("Erro", "Falha ao enviar imagem.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def display_images(image_id):
    try:
        response = requests.get(f"http://127.0.0.1:8000/image/{image_id}")
        if response.status_code == 200:
            data = response.json()
            original_path = data.get("original")
            processed_path = data.get("processed")
        
            original_image = Image.open(original_path)
            processed_image = Image.open(processed_path)
            
            original_image.thumbnail((150, 150))
            processed_image.thumbnail((150, 150))
            
            original_photo = ImageTk.PhotoImage(original_image)
            processed_photo = ImageTk.PhotoImage(processed_image)
            
            original_label.config(image=original_photo)
            original_label.image = original_photo
            processed_label.config(image=processed_photo)
            processed_label.image = processed_photo
        else:
            messagebox.showerror("Erro", "Falha ao buscar imagens.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def create_gui():
    global original_label, processed_label
    
    root = tk.Tk()
    root.title("Upload de Imagem")
    root.geometry("600x400")
    
    tk.Label(root, text="Selecione uma imagem para enviar:").pack(pady=10)
    tk.Button(root, text="Selecionar Imagem", command=select_image).pack(pady=10)
    
    original_label = tk.Label(root)
    original_label.pack(side="left", padx=10)
    
    processed_label = tk.Label(root)
    processed_label.pack(side="right", padx=10)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
