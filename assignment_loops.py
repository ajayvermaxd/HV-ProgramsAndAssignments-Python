Book1 = 499 # let book 1 is Intrduction to Python Programming
Book2 = 855 # let book 2 is Python Libraries Cookbook
Book3 = 645 # let book 3 is Data Science in Python
DeliveryCharges = 250

TotalAmount=(Book1+Book2+Book3+DeliveryCharges)
Gst= TotalAmount*0.12
print(TotalAmount)
TotalInvoice= TotalAmount+Gst
print(TotalInvoice)