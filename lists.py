states_of_INDIA = ["Maharashtra","Madhypradesh", "Goa", "Tamil Nadu", "Bihar", "Uttarpradesh" ,"Kashmir"] 

states_of_INDIA[6] = "MAHARASHTRA"
states_of_INDIA.append("Kerala")
states_of_INDIA.extend(["Gujrat","Punjab","Karnataka"])

print(states_of_INDIA)

#DIRTY_DOZEN = ["Strawberries","Spinach","Kale","Nectarines","Apples","Grapes","Peaches","Cherries","Pears","Tomatoes","Celery","Potatoes"]
fruits = ["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears",]
vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]
dirty_dozen = [fruits,vegetables] #nested lists
print(dirty_dozen[1][1])
