import streamlit as st
import pickle
from PIL import Image

def main():
    st.title(":rainbow[CUSTOMER BEHAVIOUR ON TOURISM]")
    image=Image.open('customer.jpg')
    st.image(image,width=800)

    total_likes_on_outstation_checkin_given=st.text_input(":red[total_likes_on_outstation_checkin_given]","Type here")
    
    Yearly_avg_comment_on_travel_page=st.text_input(":green[Yearly_avg_comment_on_travel_page]","Type here")
   
    total_likes_on_outofstation_checkin_received=st.text_input(":blue[total_likes_on_outofstation_checkin_received]","Type here")

    week_since_last_outstation_checkin=st.text_input(":orange[week_since_last_outstation_checkin]","Type here")
    
    montly_avg_comment_on_company_page=st.text_input("yellow[montly_avg_comment_on_company_page]","Type here")
    
    traveling_network_rating = st.text_input(":green[Traveling Network Rating]", "Type here")
   
    daily_avg_mins = st.text_input(":orange[daily_avg_mins]","Type here")

    opt=['0','1']

    following_company_page=st.radio(":orange[following_company_page]",opt)

    working_flag = st.radio(":red[Working Flag]", opt)

    adult_flag = st.radio("Adult Flag",opt)

    preferred_device_Android=st.radio(':green[preferred_device_Android]',opt)

    

    preferred_device_Laptop=st.radio(':green[preferred_device_Laptop]',opt)

    preferred_device_Mobile=st.radio(':green[preferred_device_Mobile]',opt)

    preferred_device_Others=st.radio(':green[preferred_device_Others]',opt)

    preferred_device_Tab=st.radio(':green[preferred_device_Tab]',opt)

    preferred_device_iOS=st.radio(':green[preferred_device_iOS]',opt)

    preferred_device_iOS_and_Android=st.radio(':green[preferred_device_iOS_and_Androi]',opt)



    preferred_location_type_Beach=st.radio(':green[preferred_location_type_Beach]',opt)

    preferred_location_type_Big_Cities=st.radio(':green[preferred_location_type_Big_Cities]',opt)

    preferred_location_type_Entertainment=st.radio(':green[preferred_location_type_Entertainment]',opt)

    preferred_location_type_Financial=st.radio(':green[preferred_location_type_Financial]',opt)

    preferred_location_type_Game=st.radio(':green[preferred_location_type_Game]',opt)

    preferred_location_type_Hill_Stations=st.radio(':green[preferred_location_type_Hill_Stations]',opt)

    preferred_location_type_Historical_site=st.radio(':green[preferred_location_type_Historical_site]',opt)

    preferred_location_type_Medical=st.radio(':green[preferred_location_type_Medical]',opt)

    preferred_location_type_Movie=st.radio(':green[preferred_location_type_Movie]',opt)

    preferred_location_type_OTT=st.radio(':green[preferred_location_type_OTT]',opt)

    preferred_location_type_Other=st.radio(':green[preferred_location_type_Other]',opt)

    preferred_location_type_Social_media=st.radio(':green[preferred_location_type_Social_media]',opt)

    preferred_location_type_Tour_Travel=st.radio(':green[preferred_location_type_Tour_Travel]',opt)

    preferred_location_type_Tour_and_Travel=st.radio(':green[preferred_location_type_Tour_and_Travel]',opt)

    preferred_location_type_Trekking=st.radio(':green[preferred_location_type_Trekking]',opt)


    features=[total_likes_on_outstation_checkin_given,Yearly_avg_comment_on_travel_page,
              total_likes_on_outofstation_checkin_received,week_since_last_outstation_checkin,
              montly_avg_comment_on_company_page,following_company_page,working_flag ,
              traveling_network_rating ,adult_flag ,daily_avg_mins ,preferred_device_Android,
              preferred_device_Laptop,preferred_device_Mobile,
              preferred_device_Others,preferred_device_Tab,preferred_device_iOS,
              preferred_device_iOS_and_Android,preferred_location_type_Beach,
              preferred_location_type_Big_Cities,preferred_location_type_Entertainment,
              preferred_location_type_Financial,preferred_location_type_Game,
              preferred_location_type_Hill_Stations,preferred_location_type_Historical_site,
              preferred_location_type_Medical,preferred_location_type_Movie,preferred_location_type_OTT,
              preferred_location_type_Other,preferred_location_type_Social_media,
              preferred_location_type_Tour_Travel,preferred_location_type_Tour_and_Travel,
              preferred_location_type_Trekking]

    model=pickle.load(open('modell.sav','rb'))
    standard=pickle.load(open('scalerr.sav','rb'))

    pred=st.button('PREDICT')

    if pred:
        prediction=model.predict(standard.transform([features]))

        if prediction==0:
            st.write('PRODUCT IS NOT TAKEN')

        else:
            st.write('PRODUCT IS TAKEN')
  
main()

    