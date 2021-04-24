import pandas as pd
import datetime
 
data = pd.read_csv('daily_hotel_booking_funnel.csv')

data["event_date"] = pd.to_datetime(data["event_date"], format='%Y%m%d')
data["interface_type"] = data["interface_type"].astype("str")
data["app_version"] = data["app_version"].astype("str")
data["num_visit"] = data["num_visit"].astype("int")
data["num_search"] = data["num_visit"].astype("int")
data["num_product_viewed"] = data["num_product_viewed"].astype("int")
data["num_add_to_cart"] = data["num_add_to_cart"].astype("int")
data["num_checkout"] = data["num_checkout"].astype("int")
data["num_payment_selected"] = data["num_payment_selected"].astype("int")
data["num_booking_created"] = data["num_booking_created"].astype("int")
data["num_session_visit"] = data["num_session_visit"].astype("int")
data["num_session_search"] = data["num_session_search"].astype("int")
data["num_session_product_viewed"] = data["num_session_product_viewed"].astype("int")
data["num_session_add_to_cart"] = data["num_session_add_to_cart"].astype("int")
data["num_session_checkout"] = data["num_session_checkout"].astype("int")
data["num_session_payment_selected"] = data["num_session_payment_selected"].astype("int")
data["num_session_booking_created"] = data["num_session_booking_created"].astype("int")

desc = [
    'Event Date', 
    'Interface type. Standardized values: ANDROID, IOS', 
    'Application version. Standardized format: 9.9.9',
    'Summary number of visit events',
    'Summary number of search events',
    'Summary number of product viewed events',
    'Summary number of add to cart events',
    'Summary number of checkout events',
    'Summary number of payment selected events',
    'Summary number of booking created events',
    'Summary number of visit sessions',
    'Summary number of search sessions',
    'Summary number of product viewed sessions',
    'Summary number of add to cart sessions',
    'Summary number of checkout sessions',
    'Summary number of payment selected sessions',
    'Summary number of booking created sessions']

print("Column_Name","|","Data_Type","|","Description")

a = 0
for i in data.columns:
 print(f'{i} | {data.dtypes[i]} | {desc[a]}')
 a +=1