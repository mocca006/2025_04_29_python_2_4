def main(): #主程式
    try:
            height:int = int(input('請輸入身高(公分):'))
            if height < 101 or height >220:  
                raise Exception(f"身高輸入:{height} cm, 超出100cm ~220cm 範圍") #自己建立raise檢查錯誤     
        
            weight:int = int(input('請輸入體重(公斤):'))
            if weight <30 or weight >200:       
                raise Exception(f"體重輸入:{weight} Kg, 超出30Kg ~200Kg 範圍") #自己建立raise檢查錯誤 
            
    except ValueError: #輸入格式錯誤! #特定的except #只會執行1個
            print("輸入格式錯誤!")
            #print("應用程式結束~~~")

    except Exception as e: #將其他錯誤表示出來 raise Exception("輸入超過範圍") #執行所有except
            print(e)
            print ("-"*40)
            #print("應用程式結束~~~")

    else: #try 區塊沒有except 就執行else區塊
            bmi = weight / (height/100)**2   
            
            print (f'輸入身高(公分): {height} cm')
            print (f'輸入體重(公斤): {weight} Kg')
            print ("="*30)
            print ("BMI數值計算完成")
            print (f"BMI計算數值={bmi:.2f}")
            print ()

        # BMI 值狀態描述

            if bmi < 18.5:
                print(f"BMI : {bmi: .2f}") 
                print("BMI < 18.5 , 體重過輕")

            elif bmi <= 18.5 and bmi < 24 :
                print (f"BMI計算數值={bmi:.2f}, BMI 狀態:正常範圍")

            elif  bmi <= 24 and bmi < 27 :
                print (f"BMI計算數值={bmi:.2f},BMI 狀態:體重過重")

            elif bmi <= 27 and bmi < 30 :
                print (f"BMI計算數值={bmi:.2f}, BMI 狀態:輕度肥胖")

            elif bmi <= 30 and bmi < 35 :
                print (f"BMI計算數值={bmi:.2f}, BMI 狀態:中度肥胖")

            elif bmi >=35 :
                print (f"BMI計算數值={bmi:.2f}, BMI 狀態:過度肥胖")


    print ()
    print("應用程式結束~~~")
 
if __name__ == "__main__":
    main() #執行main()
