# gradient-Descent
## coder=buildGather

Gradient Descent merupakan algoritma yang digunakan untuk mencari nilai minimum lokal yang dapat dihasilkan  
dari suatu fungsi parametrik. Teknik ini didasarkan pada fakta bahwa nilai gradien dari suatu fungsi pada 
titik tertentu menyatakan kemiringan lereng dari nilai tersebut terhadap titik di sekitarnya sehingga nilai 
minimum dapat diraih dengan mengurangi nilai titik tersebut dengan nilai gradien.
    
`x_baru` - nilai baru dari x yang akan diupdate berdasarkan nilai learning rate yang diberikan
    
`x_lama` - nilai lama yang akan diupdate dengan nilai x_baru (dalam soal ini nilai x_lama adalah 0.1) lihat
           fungsi step pada program.

`presisi` - presisi yang menentukan batas berhenti perhitungan gradient descent
    
`lr` - nilai learning rate untuk setiap step yang dibangun
    
   
### Output:
    
    1. Menampilkan nilai minimum dari x_baru yang sudah dihitung.
    2. Menampilkan jumlah steps yang dibangun dengan fungsi yang diberikan.
    3. Plot sebuah grafik yang menampilkan slope hasil dari gradient descent ini.
