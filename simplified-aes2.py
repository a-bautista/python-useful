#============================Declare functions=======================
def generate_key1(value):
    w0= (value[0:8])
    w1= (value[8:16])
    return list (w0+w1)

def my_own_xor(value1,value2):
    '''Los strings de value 3 no se pueden 
    asignar, por tanto se necesitan pasar a una lista.'''
    x=0
    if(len(value1)>8):
        value3= list('0000000000000000')
        #print "entre a mayor a 8"+str(value1)
        while(x<=15):
            if ( value1[x]=='1' and value2[x]=='1'):
                 value3[x] ='0'
            elif(value1[x]=='0' and value2[x]=='0'):
                 value3[x] ='0'
            elif(value1[x]=='1' and value2[x]=='0'):
                 value3[x] ='1'
            elif(value1[x]=='0' and value2[x]=='1'):
                 value3[x] ='1'
            else:
                print "No aplica"+str(x)+" "+str(value1[x])
            x=x+1
        return value3        
    elif (len(value1)<9 and len(value1)>4):
        value3= list('00000000')
        #print "entre a menor a 9 mayor o igual a 4"+str(value1)
        while(x<=7):
            if ( value1[x]=='1' and value2[x]=='1'):
                 value3[x] ='0'
            elif(value1[x]=='0' and value2[x]=='0'):
                 value3[x] ='0'
            elif(value1[x]=='1' and value2[x]=='0'):
                 value3[x] ='1'
            elif(value1[x]=='0' and value2[x]=='1'):
                 value3[x] ='1'
            else:
                print "No aplica"+str(x)+" "+str(value1[x])          
            x=x+1
        return value3
    elif (len(value1)<=4):
        value3= list('0000')
        #print "entre a menor o igual a 4"+str(value1)
        while(x<=3):
            if ( value1[x]=='1' and value2[x]=='1'):
                 value3[x] ='0'
            elif(value1[x]=='0' and value2[x]=='0'):
                 value3[x] ='0'
            elif(value1[x]=='1' and value2[x]=='0'):
                 value3[x] ='1'
            elif(value1[x]=='0' and value2[x]=='1'):
                 value3[x] ='1'
            else:
                print "No aplica"+str(x)+" "+str(value1[x])          
            x=x+1
        return value3 
    else:
        print "No aplica ninguno de los xors"
        return 0   
    
def generate_key2(value):
    w0	          = list (value[0:8])
    w1	          = list (value[8:16])
    resultado_xor1  = my_own_xor(w0,list ('10000000'))
    #print "Este es el primer resultado del xor=="+str(resultado_xor1)
    rotated_nibbles = rotate_nibbles(w1)
    #print "rotated nibbles==>"+str(rotated_nibbles)
    sub_nibbles     = subNib(rotated_nibbles)
    #print "estos son los subnibbles===>"+ str(sub_nibbles)    
    w2	          = my_own_xor(resultado_xor1,sub_nibbles)
    w3              = my_own_xor(w2,w1)
    return w2+w3

def generate_key3(value):
    w2		= list (value[0:8])
    w3		= list (value[8:16])
    resultado_xor_3 = my_own_xor(w2,list('00110000'))
    rotated_nibbles2= rotate_nibbles(w3)
    sub_nibbles2	= subNib(rotated_nibbles2)
    w4		= my_own_xor(resultado_xor_3,sub_nibbles2)
    w5		= my_own_xor(w4,w3)
    return w4+w5


def rotate_nibbles(value):
    if(len(value)<=8):
        w0= (value[0:4])
        w1= (value[4:8])        
        return w1+w0
    else:
        w0= (value[0:4])
        w1= (value[4:8])   
        w2= (value[8:12])
        w3= (value[12:16]) 
        return w0+w3+w2+w1  

def inverseSubNib(value):
    nibbles2 ={"1001":'0000',
    	    "0100":'0001',
    	    "1010":'0010',
    	    "1011":'0011',
    	    "1101":'0100',
    	    "0001":'0101',
    	    "1000":'0110',
    	    "0101":'0111',
    	    "0110":'1000',
    	    "0010":'1001',
    	    "0000":'1010',
    	    "0011":'1011',
    	    "1100":'1100',
    	    "1110":'1101',
    	    "1111":'1110',
    	    "0111":'1111'}
    w0             = ''.join((value[0:4]))
    w1             = ''.join((value[4:8]))
    w2             = ''.join((value[8:12]))
    w3             = ''.join((value[12:16]))
    valueAccepted1 = False
    valueAccepted2 = False      
    valueAccepted3 = False 
    valueAccepted4 = False
    previous_value = w0
    previous_value1= w1     
    previous_value01=w0
    previous_value11=w1
    #This loop is Iterating each item, one item that passed cannot be 
    #recovered again. Really??? You need to give more proofs about this.
    for nibble,s_box in nibbles2.iteritems():
        if (nibble==w0 and (valueAccepted1==False)):
            w0             = s_box
            valueAccepted1 = True
            if (previous_value==w2):
                w2=w0
                valueAccepted3=True
                if (previous_value01==w3):
                    w3=w0
                    valueAccepted4=True
        elif (nibble==w1 and valueAccepted2==False):
            w1		 = s_box
            valueAccepted2 = True
            if (previous_value1==w2):
                w2=w1
                valueAccepted3=True
            if (previous_value11==w3):
                w3=w1
                valueAccepted4=True
        elif (nibble==w2 and valueAccepted3==False):
            w2=s_box
            valueAccepted3=True    
        elif (nibble==w3 and valueAccepted4==False):
            w3=s_box
            valueAccepted4=True
        else:
               print "Encryption process..." 
    return list(w0+w1+w2+w3)        
    
def subNib(value):
    """Es necesario juntar las listas ya que de lo contrario
    no se podra conocer el valor con su definicion. Por otro 
    lado,es necesario volver a dejar las listas como estaban.
    Recuerda que en un diccionario siempre buscas dos palabas,
    la palabra y el significado, por tanto, en este diccionario
    tengo la variable nibble y su definicion en la variable s_box.
    Al parecer, los diccionarios solo permiten que un valor sea tomado,
    si el mismo valor aparece ya no sera tomado."""   
    nibbles = {"0000":'1001',
	 "0001":'0100',
	 "0010":'1010',
	 "0011":'1011',
	 "0100":'1101',
	 "0101":'0001',
	 "0110":'1000',
	 "0111":'0101',
	 "1000":'0110',
	 "1001":'0010',
	 "1010":'0000',
	 "1011":'0011',
	 "1100":'1100',
	 "1101":'1110',
	 "1110":'1111',
	 "1111":'0111'}
    """Se necesita una bandera ya que de lo contrario el ciclo puede 
    cambiar el valor de algun simbolo que ya habia sido cambiado."""
    if (len(value)<=8):
        w0             = ''.join((value[0:4]))
        w1             = ''.join((value[4:8]))  
        valueAccepted1 = False
        valueAccepted2 = False        
        for nibble,s_box in nibbles.iteritems():
            if (str(nibble)==str(w0) and (valueAccepted1==False)):
                w0=s_box
                valueAccepted1=True
            elif (str(nibble)==str(w1) and (valueAccepted2==False)):
                w1=s_box
                valueAccepted2=True
            else:
                print "Encryption process..."        
        return list(w0+w1)
    else:
        w0             = ''.join((value[0:4]))
        w1             = ''.join((value[4:8]))
        w2             = ''.join((value[8:12]))
        w3             = ''.join((value[12:16]))
        previous_value = w0
        previous_value1= w1     
        previous_value01=w0
        previous_value11=w1
        valueAccepted1 = False
        valueAccepted2 = False      
        valueAccepted3 = False 
        valueAccepted4 = False
        for nibble,s_box in nibbles.iteritems():
            if (str(nibble)==str(w0) and (valueAccepted1==False)):
	      #previous_value = w0
                w0             = s_box
                valueAccepted1 = True
                #print "entre a 1 de nibbles y sustitui"
                if (str(previous_value)==str(w2)):
                    w2=w0
                    valueAccepted3=True
                    #print "entre a subnivel 1 de nibbles y sustitui"
                if (str(previous_value01)==str(w3)):
                    w3=w0
                    valueAccepted4=True
                    #print "entre a sub-subnivel de nibbles y sustitui"
            elif (str(nibble)==str(w1) and (valueAccepted2==False)):
	      #previous_value1=w1
                w1		 = s_box
                valueAccepted2 = True
                #print "entre a 2 de nibbles y sustitui"
                if (str(previous_value1)==str(w2)):
                    w2=w1
                    valueAccepted3=True
                    #print "entre a subnivel 2 de nibbles y sustitui"
                if (str(previous_value11)==str(w3)):
                    w3=w1
                    valueAccepted4=True
                    #print "entre a sub-subnivel 2 de nibbles y sustitui"
            elif (str(nibble)==str(w2) and (valueAccepted3==False)):
                w2=s_box
                valueAccepted3=True    
                #print "entre a 3 de nibbles y sustitui"            
            elif (str(nibble)==str(w3) and (valueAccepted4==False)):
                w3=s_box
                valueAccepted4=True    
                #print "entre a 4 de nibbles y sustitui"            
            else:
               print "Encryption process..." 
        return list(w0+w1+w2+w3)    

def lookfor(value):
    """Esta es la definicion de cada numero multiplicado por otro numero en un
    campo extendido de Galois para 2^4"""
    extended_field = {"00000000":'0000',
	 "00000001":'0000',
	 "00000010":'0000',
	 "00000011":'0000',
	 "00000100":'0000',
	 "00000101":'0000',
	 "00000110":'0000',
	 "00000111":'0000',
	 "00001000":'0000',
	 "00001001":'0000',
	 "00001010":'0000',
	 "00001011":'0000',
	 "00001100":'0000',
	 "00001101":'0000',
	 "00001110":'0000',
	 "00001111":'0000',#     Fin de la multiplicacion para 0
	 "00010000":'0000',#0
	 "00010001":'0001',#1
	 "00010010":'0010',#2
	 "00010011":'0011',#3
	 "00010100":'0100',#4
	 "00010101":'0101',#5
	 "00010110":'0110',#6
	 "00010111":'0111',#7
	 "00011000":'1000',#8
	 "00011001":'1001',#9
	 "00011010":'1010',#10
	 "00011011":'1011',#11
	 "00011100":'1100',#12
	 "00011101":'1101',#13
	 "00011110":'1110',	#14
	 "00011111":'1111',#15    Fin de la multiplicacion para 1	 
	 "00100000":'0000',
	 "00100001":'0010',
	 "00100010":'0100',
	 "00100011":'0110',
	 "00100100":'1000',
	 "00100101":'1010',
	 "00100110":'1100',
	 "00100111":'1110',
	 "00101000":'0011',
	 "00101001":'0001',
	 "00101010":'0111', #  7
	 "00101011":'0101', #  5
	 "00101100":'1011', #  B
	 "00101101":'1001', #  9
	 "00101110":'1111',	 #  F
	 "00101111":'1101', #  D  Fin de la multiplicacion para 2
	 "00110000":'0000',
	 "00110001":'0011',
	 "00110010":'0110', #6
	 "00110011":'0101', #5
	 "00110100":'1100', #C
	 "00110101":'1111',
	 "00110110":'1010',
	 "00110111":'1001',
	 "00111000":'1011',
	 "00111001":'1000',
	 "00111010":'1101',
	 "00111011":'1110',
	 "00111100":'0111',
	 "00111101":'0100',
	 "00111110":'0001',	 
	 "00111111":'0010',#    Fin de la multiplicacion para 3	 	 	 	 
	 "01000000":'0000',
	 "01000001":'0100', # 
	 "01000010":'1000', # 8
	 "01000011":'1100', # C
	 "01000100":'0011', # 3
	 "01000101":'0111', # 7
	 "01000110":'1011', # B
	 "01000111":'1111', # F
	 "01001000":'0110', # 6
	 "01001001":'0010', # 2
	 "01001010":'1110', # E
	 "01001011":'1010', # A
	 "01001100":'0101', # 5
	 "01001101":'0001', # 1
	 "01001110":'1101',	 # D
	 "01001111":'1001', # 9   Fin de la multiplicacion para 4	
	 "01010000":'0000',
	 "01010001":'0101', # 5
	 "01010010":'1010', # A
	 "01010011":'1111', # F
	 "01010100":'0111', # 7
	 "01010101":'0010', # 2
	 "01010110":'1101', # D
	 "01010111":'1000', # 8
	 "01011000":'1110', # E
	 "01011001":'1011', # B
	 "01011010":'0100', # 4
	 "01011011":'0001', # 1
	 "01011100":'1001', # 9
	 "01011101":'1100', # C
	 "01011110":'0011',	 # 3
	 "01011111":'0110', # 6   Fin de la multiplicacion para 5	
	 "01100000":'0000',
	 "01100001":'0110', 
	 "01100010":'1100', #C
	 "01100011":'1010', #A
	 "01100100":'1011', #B
	 "01100101":'1101', #D
	 "01100110":'0111', #7
	 "01100111":'0001', #1
	 "01101000":'0101', #5
	 "01101001":'0011', #3
	 "01101010":'1001', #9
	 "01101011":'1111', #F
	 "01101100":'1110', #E
	 "01101101":'1000', #8
	 "01101110":'0010',	 #2
	 "01101111":'0100', #4    Fin de la multiplicacion para 6	
	 "01110000":'0000',
	 "01110001":'0111', 
	 "01110010":'1110', #E
	 "01110011":'1001', #9
	 "01110100":'1111', #F
	 "01110101":'1000', #8
	 "01110110":'0001', #1
	 "01110111":'0110', #6
	 "01111000":'1101', #D
	 "01111001":'1010', #A
	 "01111010":'0011', #3
	 "01111011":'0100', #4
	 "01111100":'0010', #2
	 "01111101":'0101', #5
	 "01111110":'1100',	 #C
	 "01111111":'1011', #B    Fin de la multiplicacion para 7	
	 "10000000":'0000',
	 "10000001":'1000', 
	 "10000010":'0011', #3
	 "10000011":'1011', #B
	 "10000100":'0110', #6
	 "10000101":'1110', #E
	 "10000110":'0101', #5
	 "10000111":'1101', #D
	 "10001000":'1100', #C
	 "10001001":'0100', #4
	 "10001010":'1111', #F
	 "10001011":'0111', #7
	 "10001100":'1010', #A
	 "10001101":'0010', #2
	 "10001110":'1001',	 #9
	 "10001111":'0001', #1    Fin de la multiplicacion para 8	
	 "10010000":'1001',
	 "10010001":'1001', 
	 "10010010":'0001', #1
	 "10010011":'1000', #8
	 "10010100":'0010', #2
	 "10010101":'1011', #B
	 "10010110":'0011', #3
	 "10010111":'1010', #A
	 "10011000":'0100', #4
	 "10011001":'1101', #D
	 "10011010":'0101', #5
	 "10011011":'1100', #C
	 "10011100":'0110', #6
	 "10011101":'1111', #F
	 "10011110":'0111',	 #7
	 "10011111":'1110', #E    Fin de la multiplicacion para 9	
	 "10100000":'0000',
	 "10100001":'1010', 
	 "10100010":'0111', #7
	 "10100011":'1101', #D
	 "10100100":'1110', #E
	 "10100101":'0100', #4
	 "10100110":'1001', #9
	 "10100111":'0011', #3
	 "10101000":'1111', #F
	 "10101001":'0101', #5
	 "10101010":'1000', #8
	 "10101011":'0010', #2
	 "10101100":'0001', #1
	 "10101101":'1011', #B
	 "10101110":'0110',	 #6
	 "10101111":'1100', #C    Fin de la multiplicacion para 10
	 "10110000":'0000',
	 "10110001":'1011', 
	 "10110010":'0101', #5
	 "10110011":'1110', #E
	 "10110100":'1010', #A
	 "10110101":'0001', #1
	 "10110110":'1111', #F
	 "10110111":'0100', #4
	 "10111000":'0111', #7
	 "10111001":'1100', #C
	 "10111010":'0010', #2
	 "10111011":'1001', #9
	 "10111100":'1101', #D
	 "10111101":'0110', #6
	 "10111110":'1000',	 #8
	 "10111111":'0011', #3    Fin de la multiplicacion para 11	
	 "11000000":'0000',
	 "11000001":'1100', 
	 "11000010":'1011', #B
	 "11000011":'0111', #7
	 "11000100":'0101', #5
	 "11000101":'1001', #9
	 "11000110":'1110', #E
	 "11000111":'0010', #2
	 "11001000":'1010', #A
	 "11001001":'0110', #6
	 "11001010":'0001', #1
	 "11001011":'1101', #D
	 "11001100":'1111', #F
	 "11001101":'0011', #3
	 "11001110":'0100',	 #4
	 "11001111":'1000', #8    Fin de la multiplicacion para 12	
	 "11010000":'0000',
	 "11010001":'1101', 
	 "11010010":'1001', #9
	 "11010011":'0100', #4
	 "11010100":'0001', #1
	 "11010101":'1100', #C
	 "11010110":'1000', #8
	 "11010111":'0101', #5
	 "11011000":'0010', #2
	 "11011001":'1111', #F
	 "11011010":'1011', #B
	 "11011011":'0110', #6
	 "11011100":'0011', #3
	 "11011101":'1110', #E
	 "11011110":'1010',	 #A
	 "11011111":'0111', #7    Fin de la multiplicacion para 13	
	 "11100000":'0000',
	 "11100001":'1110', 
	 "11100010":'1111', #F
	 "11100011":'0001', #1
	 "11100100":'1101', #D
	 "11100101":'0011', #3
	 "11100110":'0010', #2
	 "11100111":'1100', #C
	 "11101000":'1001', #9
	 "11101001":'0111', #7
	 "11101010":'0110', #6
	 "11101011":'1000', #8
	 "11101100":'0100', #4
	 "11101101":'1010', #A
	 "11101110":'1011',	 #B
	 "11101111":'0101', #5    Fin de la multiplicacion para 14
	 "11110000":'0000',
	 "11110001":'1111', 
	 "11110010":'1101', #D
	 "11110011":'0010', #2
	 "11110100":'1001', #9
	 "11110101":'0110', #6
	 "11110110":'0100', #4
	 "11110111":'1011', #B
	 "11111000":'0001', #1
	 "11111001":'1110', #E
	 "11111010":'1100', #C
	 "11111011":'0011', #3
	 "11111100":'1000', #8
	 "11111101":'0111', #7
	 "11111110":'0101',	 #5
	 "11111111":'1010',} #A    Fin de la multiplicacion para 15	 
    for binary_digit,result in extended_field.iteritems():   
        if(binary_digit==value):
            value=result
    return value 

def inverse_fake_matrix(value):
    s00       = ''.join(value[0:4])
    s10       = ''.join(value[4:8])
    s01	    = ''.join(value[8:12])
    s11       = ''.join(value[12:16])

    s00_solve = lookfor('1001'+s00)
    s00_solve2= lookfor('0010'+s10)
    result_xor= my_own_xor(s00_solve,s00_solve2)
        
    s10_solve = lookfor('0010'+s00)
    s10_solve2= lookfor('1001'+s10)
    result_xor2= my_own_xor(s10_solve,s10_solve2)    
    
    s01_solve = lookfor('1001'+s01)
    s01_solve2= lookfor('0010'+s11)
    result_xor3= my_own_xor(s01_solve,s01_solve2)
    
    s11_solve = lookfor('0010'+s01)
    s11_solve2= lookfor('1001'+s11)
    result_xor4= my_own_xor(s11_solve,s11_solve2)
    
    return list(result_xor+result_xor2+result_xor3+result_xor4)   

def fake_matrix_operation(value):
    s00       = ''.join(value[0:4])
    s10       = ''.join(value[4:8])
    s01	    = ''.join(value[8:12])
    s11       = ''.join(value[12:16])

    s00_solve = lookfor('0001'+s00)
    s00_solve2= lookfor('0100'+s10)
    result_xor= my_own_xor(s00_solve,s00_solve2)
        
    s10_solve = lookfor('0100'+s00)
    s10_solve2= lookfor('0001'+s10)
    result_xor2= my_own_xor(s10_solve,s10_solve2)    
    
    s01_solve = lookfor('0001'+s01)
    s01_solve2= lookfor('0100'+s11)
    result_xor3= my_own_xor(s01_solve,s01_solve2)
    
    s11_solve = lookfor('0100'+s01)
    s11_solve2= lookfor('0001'+s11)
    result_xor4= my_own_xor(s11_solve,s11_solve2)
    
    return list(result_xor+result_xor2+result_xor3+result_xor4)

    
#=============================Initiate program =====================================    
plaintext  	=  raw_input("Please, provide the following binary 16 characters:")
mother_key 	=  raw_input("Please, provide the following binary key of 16 characters:")

#=====================Encryption=========================
K1=generate_key1(mother_key)
K2=generate_key2(mother_key)
K3=generate_key3(K2)
print "Key 1"+str(K1)
print "Key 2"+str(K2)
print "Key 3"+str(K3)
print "Plaintext ===>"+str(plaintext)
print "Master key==> "+str(mother_key)
print "=========>Encryption is being performed...<=========="
round1=rotate_nibbles(subNib(my_own_xor(plaintext,K1)))
round2=(subNib(my_own_xor(fake_matrix_operation(round1),K2)))
round2=rotate_nibbles(subNib(my_own_xor(fake_matrix_operation(round1),K2)))
print "Round 2 "+str(round2)
print "Round 3: This is the ciphertext==>"+str(my_own_xor(round2,K3))

#======================Decryption=============================
ciphertext=my_own_xor(round2,K3)
Decrypt1=my_own_xor(ciphertext,K3)
Decrypt1=my_own_xor(inverseSubNib(rotate_nibbles(inverse_fake_matrix(my_own_xor(rotate_nibbles(inverseSubNib(Decrypt1)),K2)))),K1)
print "Decryption done==> "+str(Decrypt1)
