import streamlit as st
import pandas as pd
import test as tt





comp=tt.competitor()

comp_df=pd.DataFrame(comp,columns=['competitor_id','name','country','country_code','abbreviation'])

call=tt.sidebar()
side_df=pd.DataFrame(call,columns=['competition_id','competition_name','type','gender','category_id'])

cat=tt.category()
cat_df=pd.DataFrame(cat,columns=['category_id','category_name'])

ran=tt.ranking()
ran_df=pd.DataFrame(ran,columns=['rank_id','rank','movement','points','competitons_played','competitor_id'])

ven=tt.venues()
ven_df=pd.DataFrame(ven,columns=['venue_id','venue_name','city_name','country_name','country_code','timezone','complex_id'])

customize=tt.cust1()
cost_df=pd.DataFrame(customize,columns=['competitor_id',"name",'rank'])

customize=tt.cust2()
cost_df2=pd.DataFrame(customize,columns=['competitor_id',"name",'rank'])

customize=tt.cust3()
cost_df3=pd.DataFrame(customize,columns=['competitor_id',"name",'rank'])

point=tt.points()
points_df=pd.DataFrame(point,columns=['name','points'])


#=============================================================================================================================

st.sidebar.image("F:/project_tennis/tenn.jpg",width=170,)

st.sidebar.header("CHOOSE OPTION")
h=st.sidebar.selectbox("",["HOME","MENU","ABOUT ME"])



if h=="HOME":
    st.header("🎾 Welcome to my Tennis page!")
    
    st.subheader("TOTAL NO OF COMPETITORS")
    st.selectbox("COMPETITOR LIST",comp_df['name'])

    st.subheader("TOTAL NO OF COUNTRY REPRESENTED")
    st.selectbox('COUNTRY LIST',comp_df['country'])


if h=="MENU":
    main=st.selectbox("SELECT OPTION",['About Competition',
                                       'About categories',
                                       'About competitor rankings',
                                       'About venues',
                                       'Leaderboard'])

    if main=="About Competition":
        
        gen=st.multiselect(
            "SELECT GENDER",
            options=side_df['gender'].unique(),
            
            #default=side_df['gender'].unique(),

        )      
        

        type=st.multiselect(
            "SELECT TYPE",
            options=side_df['type'].unique(),
            #default=side_df['type'].unique()
        )

        filtered_df = side_df[
        (side_df["gender"].isin(gen)) &  # Filter for gender
        (side_df["type"].isin(type))    # Filter for type
            ]

        st.write(filtered_df)

        

    if main=="About categories":
        
        st.write(cat_df)

    if main=='About competitor rankings':

        rank=st.slider(
            label="SELECT RANK",
            min_value=0,
            max_value=20,
            value=(0,1),
            step=2)
        
        lower_bound, upper_bound = rank
        st.write(f"Rank From {lower_bound} To {upper_bound}")

        #lower_bound, upper_bound = rank  # Unpack the range
        slid_df = ran_df[(ran_df["rank"] >= lower_bound) & (ran_df["rank"] <= upper_bound)]

        st.write(slid_df)

        
        

    if main=="About venues":

        coun=st.multiselect(
            "SELECT COUNTRY NAME",
            options=ven_df["country_name"].unique())

        filtered_coun=ven_df[ven_df["country_name"].isin(coun)]

        st.dataframe(filtered_coun)

    
    if main=="Leaderboard":


        top=st.radio("SELECT TOP PLAYERS",
                 options=["NONE","TOP 3 PLAYERS", "TOP 5 PLAYERS","TOP 10 PLAYERS"],
                 index=0)
        
        st.markdown("If You Want To See Points Please Choose None In Above")

        pp=st.radio("SELECT TOP POINTS",
                 options=['NONE','TOP 3','TOP 5'],
                 index=0)
                    

           
        
        if top=="NONE":
            if pp=="TOP 3":
                x=points_df.nlargest(3,"points")
                st.write(x)

            elif pp=="TOP 5":
                x=points_df.nlargest(5,"points")
                st.write(x)
            

        elif top=="TOP 3 PLAYERS":

            st.write(cost_df)

        elif top=="TOP 5 PLAYERS":

            st.write(cost_df2)

        elif top=="TOP 10 PLAYERS":

            st.write(cost_df3)

        

if h=='ABOUT ME':

    st.header("Hi!  i'm Vignesh kumar ")

    st.markdown("Thanks For Visiting My Webpage")

    st.markdown("I Hope You Like My Creation")

    


    st.markdown("E-MAIL: wikki1304@gmail.com")

    st.markdown("""
    <p style="text-align:center;">
        &copy; [2025] [VIGNESH KUMAR S]. All rights reserved.
    </p>
""", unsafe_allow_html=True)
    


        

        

        

        

        

        

      


        

            











                                


                                
                                
                                
