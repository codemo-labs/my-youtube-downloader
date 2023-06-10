from flask import Flask, request, Response, render_template

impor youtube_dl

aplikasi = Labu(__nama__)

@aplikasi.rute('/')

def rumah():

    kembalikan render_template('index.html')

    

# menahan permintaan unduhan

@ aplikasi.rute('/unduh', metode=['POST'])

unduhan def ():

    url = permintaan.form['url']

    ydl_opts = {

        'format': 'video terbaik+audio terbaik/terbaik',

        'outtmpl': '%(title)s.%(ext)s',

    }

    mencoba:

        dengan youtube_dl.YoutubeDL(ydl_opts) sebagai ydl:

            ydl.download([url])

            return Response('Video berhasil diunduh', status=200)

    kecuali:

        return Response('Terjadi kesalahan saat mengunduh video', status=500)

jika __nama__ == '__main__':

    app.run(debug=True)

