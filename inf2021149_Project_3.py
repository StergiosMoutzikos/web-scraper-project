import tkinter as tk  #Για δημιουργία γραφικών περιβαλλόντων
from tkinter import messagebox  #Για εμφάνιση μηνυμάτων
from tkinter import ttk  #Για προηγμένους ελέγχους εμφάνισης
import matplotlib.pyplot as plt  # Εισαγωγή της βιβλιοθήκης matplotlib.pyplot για τη δημιουργία γραφικών
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  #Για ενσωμάτωση γραφικών matplotlib σε παράθυρο tkinter
import requests  #Για αποστολή HTTP αιτημάτων
from bs4 import BeautifulSoup  #Για ανάλυση HTML
import csv  #Για εργασία με αρχεία CSV
from textstat import flesch_reading_ease  #Για υπολογισμό ευκολίας ανάγνωσης κειμένου

def scrape_website(url):
    try:
        response = requests.get(url)  # Αίτημα GET προς τον δοσμένο URL
        response.raise_for_status()  # Έλεγχος για σφάλματα κατά την ανάκτηση του περιεχομένου της σελίδας
        page_content = response.text  # Κείμενο της σελίδας σε μορφή κειμένου
        soup = BeautifulSoup(page_content, 'html.parser')  # Δημιουργία αντικειμένου Beautiful Soup για ανάλυση HTML

        text_content = soup.get_text()  # Εξαγωγή κειμένου από την HTML

        # Εξαγωγή μεταδεδομένων (π.χ., τίτλου, περιγραφής)
        title = soup.title.string.strip() if soup.title else ""  # Τίτλος σελίδας, αν υπάρχει
        description = soup.find('meta', attrs={'name': 'description'})  # Αναζήτηση μεταδεδομένων περιγραφής
        description = description.get('content').strip() if description else ""  # Περιγραφή σελίδας, αν υπάρχει

        # Εύρεση στοιχείων εικόνας και εξαγωγή των συνδέσμων τους
        image_elements = soup.find_all('img')  # Αναζήτηση όλων των στοιχείων εικόνας
        image_urls = [img.get('src') for img in image_elements]  # Εξαγωγή των URLs των εικόνων

        # Εύρεση στοιχείων υπερσυνδέσμων και εξαγωγή των συνδέσμων τους
        hyperlink_elements = soup.find_all('a')  # Αναζήτηση όλων των στοιχείων υπερσυνδέσμων
        hyperlink_urls = [a.get('href') for a in hyperlink_elements]  # Εξαγωγή των URLs των υπερσυνδέσμων
        num_images = len(image_urls)  # Πλήθος εικόνων
        text_length = len(text_content)  # Μήκος κειμένου
        num_words = len(text_content.split())  # Πλήθος λέξεων
        unique_words = len(set(text_content.split()))  # Πλήθος μοναδικών λέξεων
        readability_score = flesch_reading_ease(text_content)  # Υπολογισμός σκορ διαβασιμότητας

        # Επιστροφή των δεδομένων σε μορφή λεξικού
        return {
            'url': url,
            'text_content': text_content,
            'title': title,
            'description': description,
            'num_images': num_images,
            'image_urls': image_urls,
            'text_length': text_length,
            'num_words': num_words,
            'unique_words': unique_words,
            'readability_score': readability_score,
            'num_hyperlinks': len(hyperlink_urls),
            'hyperlink_urls': hyperlink_urls
        }
    except Exception as e:
        # Αν προκύψει κάποιο σφάλμα κατά την ανάκτηση δεδομένων, εμφάνιση μηνύματος
        print(f"Προέκυψε σφάλμα κατά την ανάκτηση δεδομένων από τον ιστότοπο {url}: {e}")
        return {}

def save_to_csv(data, filename):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as output_file:
            writer = csv.writer(output_file)

            # Εγγραφή αναλύσεων στο CSV
            writer.writerow(["Analysis", "Value"])
            writer.writerow(["Number of Images", data.get('num_images', '')])
            writer.writerow(["Text Length", data.get('text_length', '')])
            writer.writerow(["Number of Words", data.get('num_words', '')])
            writer.writerow(["Number of Unique Words", data.get('unique_words', '')])
            writer.writerow(["Readability Score", data.get('readability_score', '')])
            writer.writerow(["Number of Hyperlinks", data.get('num_hyperlinks', '')])
            writer.writerow([])  # Προσθήκη κενής γραμμής για διαχωρισμό

            # Εγγραφή μεταδεδομένων στο CSV+++
            writer.writerow(["Metadata", "Value"])
            for key, value in data.items():
                writer.writerow([key, value])
        messagebox.showinfo("Success", "Website data has been saved to website_data.csv")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving data to CSV: {e}")

def display_gui():
    def scrape_and_display():
        url = url_entry.get()  # Λήψη του URL
        website_data = scrape_website(url)  # Ανάκτηση δεδομένων 
        if website_data:
            save_to_csv(website_data, 'website_data.csv')  # Αποθήκευση των δεδομένων σε CSV
            plot_graph(website_data)  # Εμφάνιση γραφήματος των δεδομένων
            root.destroy()  # Κλείσιμο του παραθύρου GUI μετά την αποθήκευση των δεδομένων

    def plot_graph(data):
        categories = ['Number of Words', 'Number of Unique Words', 'Number of Hyperlinks', 'Number of Images']
        values = [data.get('num_words', 0), data.get('unique_words', 0), data.get('num_hyperlinks', 0), data.get('num_images', 0)]

        plt.figure(figsize=(8, 5))
        bars = plt.bar(categories, values, color=['blue', 'green', 'orange', 'red'])

        # Προσθήκη αρίθμησης σε κάθε μπάρα
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom')

        plt.xlabel('Categories')
        plt.ylabel('Count')
        plt.title('Website Data')
        plt.xticks(rotation=45)  #Για καλύτερη αναγνωσιμότητα
        plt.tight_layout()  #Για να μην γίνεται περικοπή στις ετικέτες
        plt.show()

    root = tk.Tk()  # Δημιουργία του κύριου GUI
    root.title("Website Scraper")

    
    style = ttk.Style()
    style.theme_use('clam')  # Ορισμός του στυλ σε 'clam'

    # Πλαίσιο
    main_frame = ttk.Frame(root)
    main_frame.pack(padx=20, pady=20)

    # Καταχώρηση URL
    url_label = ttk.Label(main_frame, text="Enter the URL of the website:")
    url_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    url_entry = ttk.Entry(main_frame, width=50)
    url_entry.grid(row=0, column=1, padx=10, pady=10)

    scrape_button = ttk.Button(main_frame, text="Retrieve Website Data", command=scrape_and_display)
    scrape_button.grid(row=0, column=2, padx=10, pady=10)

    root.mainloop()  # Έναρξη εκτέλεσης του GUI

if __name__ == "__main__":
    display_gui()  # Κλήση της συνάρτησης για την εμφάνιση του GUI