import pickle
import streamlit as st
import requests
import pandas as pd


def recommend(job):
    job_index = jobs[jobs['Title'] == job].index[0]
    distances = similarity[job_index]
    jobs_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_jobs = []
    for i in jobs_list:
        recommended_jobs.append(jobs.iloc[i[0]].Title)
    return recommended_jobs

pd.set_option('display.max_colwidth', 1000)
org_df = pd.read_csv('finaldf.csv')
def exrtract_url(jobname):
     link=org_df.loc[org_df['Title'] == jobname, 'Image']
     listh = link.tolist()
     return listh

def exrtractlink_url(jobname):
     link=org_df.loc[org_df['Title'] == jobname, 'ugccard__wrap__2dpy7_URL']
     listhur = link.tolist()
     return listhur

def exrtractcreator(jobname):
     link=org_df.loc[org_df['Title'] == jobname, 'User']
     return link

jobs_dict = pickle.load(open('jobsdict.pkl','rb'))
jobs = pd.DataFrame(jobs_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Rockstar Gta5 Stunt Races Jobs Recommendation System 🎮")
st.subheader("Problem Statement:- It's a Hard task to find the best Races for Content Creators. Here is the solution. The difference Between This and the Social club website is the Result. If we search for a race on a social club then we got the particular stunt race or job but in this, we got recommend races or jobs.")

st.markdown("""-------------------------------------""")

st.header(":sunglasses: Select Job or Race :sunglasses:")

selected_job = st.selectbox(
    "Type or select a job from the dropdown",jobs['Title'].values
)

if st.button('Show Recommendation 👈'):
    st.header(":sunglasses: Your Selected Stunt Race Job :sunglasses:")
    st.subheader(selected_job)
    mapimg = exrtract_url(selected_job)
    st.image(mapimg,width=500)

    st.markdown("""-------------------------------------""")
    st.header(":sunglasses: Recommendation Jobs :sunglasses:")

    recommendations = recommend(selected_job)
    print(recommendations[0])
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(recommendations[0])
        st.image(exrtract_url(recommendations[0]))
        st.write("Creator:- " ,exrtractcreator(recommendations[0]).values[0])
        url = exrtractlink_url(recommendations[0])
        button_label = 'Bookmark Job!'
        link = f'<a href="{url[0]}" target="_blank">{button_label}</a>'
        st.markdown(link, unsafe_allow_html=True)

    with col2:
        st.write(recommendations[1])
        st.image(exrtract_url(recommendations[1]))
        url = exrtractlink_url(recommendations[1])
        st.write("Creator:- " ,exrtractcreator(recommendations[1]).values[0])
        button_label = 'Bookmark Job!'
        link = f'<a href="{url[0]}" target="_blank">{button_label}</a>'
        st.markdown(link, unsafe_allow_html=True)

    with col3:
        st.write(recommendations[2])
        st.image(exrtract_url(recommendations[2]))
        url = exrtractlink_url(recommendations[2])
        st.write("Creator:- " ,exrtractcreator(recommendations[2]).values[0])
        button_label = 'Bookmark Job!'
        link = f'<a href="{url[0]}" target="_blank">{button_label}</a>'
        st.markdown(link, unsafe_allow_html=True)

    with col4:
        st.write(recommendations[3])
        st.image(exrtract_url(recommendations[3]))
        url = exrtractlink_url(recommendations[3])
        st.write("Creator:- " ,exrtractcreator(recommendations[3]).values[0])
        button_label = 'Bookmark Job!'
        link = f'<a href="{url[0]}" target="_blank">{button_label}</a>'
        st.markdown(link, unsafe_allow_html=True)

    with col5:
        st.write(recommendations[4])
        st.image(exrtract_url(recommendations[4]))
        url = exrtractlink_url(recommendations[4])
        st.write("Creator:- " ,exrtractcreator(recommendations[4]).values[0])
        button_label = 'Bookmark Job!'
        link = f'<a href="{url[0]}" target="_blank">{button_label}</a>'
        st.markdown(link, unsafe_allow_html=True)



        
