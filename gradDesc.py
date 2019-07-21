import matplotlib.pyplot as plt


function = lambda x : (x**5)-(3*(x**3))-(2*(x**2))+10
def turunan(x):
    
    '''    
    Initial:
    x - nilai numerik dari fungsi x yang sudah dibuat
    
    Return:
    x_turunan - nilai turunan x dari fungsi yang dibuat
    
    '''
    
    turunan = 5*(x**4)-(9*(x**2))-(4*x)
    return turunan


def step(x_baru, x_lama, presisi, lr):
    
    '''
    
    x_baru - nilai baru dari x yang akan diupdate berdasarkan nilai learning rate yang diberikan
    
    x_lama - nilai lama yang akan diupdate dengan nilai x_baru (dalam soal ini nilai x_lama adalah 0.1) lihat
             fungsi step dibawah.
    
    presisi - presisi yang menentukan batas berhenti perhitungan gradient descent
    
    lr - nilai learning rate untuk setiap step yang dibangun
    
    '''
    
    
    x_list, y_list = [x_baru], [function(x_baru)] 
    # fungsi looping selama kondisi abs memenuhi syarat, yaitu > presisi
    while abs(x_baru - x_lama) > presisi:
        
        # update nilai x
        x_lama = x_baru
        
        # mendapatkan nilai turunan dari x
        d_x = - turunan(x_lama)
        
        # update nilai x dengan menambahkan x_lama dengan learning rate dikali turunan x
        x_baru = x_lama + (lr * d_x)
        
        # fungsi dot pada plot yang akan dihasilkan
        x_list.append(x_baru)
        y_list.append(function(x_baru))

    print ("Nilai local minimumnya adalah: "+ str(x_baru))
    print ("Jumlah step: " +str(len(x_list)))
    print (x_list)
    
    plt.subplot(1,2,1)
    plt.scatter(x_list,y_list,c="g")
    plt.plot(x_list,y_list,c="b")
    plt.title("Plot Gradient Descent")
    plt.show()


step(0.15, 0.1, 0.001, 0.05)
