from tkinter import * 
from pytube import YouTube
from tkinter import messagebox, filedialog, ttk

def video():
    link= urlval.get()
    download_folder= destination.get()
    qual= choice.get()

    getvid= YouTube(link)        

    if qual !="mp3":
        vidstream= getvid.streams.filter(res=qual).first()

    else:
        vidstream= getvid.streams.filter(only_audio=True).first()

    vidstream.download(download_folder)


    messagebox.showinfo('Successful!', f"Downloaded Successfully in {download_folder}")


def browse():
    download_dir= filedialog.askdirectory(initialdir='Select your Directory')
    destination.set(download_dir)

root= Tk()
root.geometry('400x450')
root.maxsize(400, 450)
root.title('Youtube Downloader by Twarit')
root.configure(background='grey')

intro= Label(root, text='Youtube Downloader- Audio/Video', font='lucida 15 bold', bg='black', fg='white')
intro.pack(ipady=5, pady=10, ipadx=10)

text1= Label(root, text='Enter the link of the youtube video: ',font='lucida 10 bold', bg='grey' )
text1.pack(pady=20)


urlval= StringVar()

url= Entry(root, textvariable=urlval, width=60)
url.pack(ipadx=5, ipady=7)

text2= Label(root, text='Destination Folder: ',font='lucida 10 bold', bg='grey' )
text2.pack(pady=20)

destination= StringVar()

dest= Entry(root, textvariable=destination, width=40)
dest.pack(ipadx=5, ipady=7, anchor='n', padx=15)

browsee= Button(root, text='Browse', bg='lightgreen', command=browse)
browsee.pack(ipadx=5, ipady=5, pady=10)

quality= Label(root, text='Select Quality: ', font='lucida 15 bold', bg='grey')
quality.pack(ipadx=10)

choices= ['240p', '360p', '720p', '1080p', 'mp3']
choice= ttk.Combobox(root, values=choices)
choice.pack()


b1= Button(root, text='Download', command=video, font='lucida 12 bold ', bg='red', fg='white')
b1.pack( padx=10, ipadx=10, anchor='n', pady=20)








root.mainloop()