
import streamlit as st

class User:
  def __init__(self, name, email, skill_offer, skill_want):
    self.name = name
    self.email = email
    self.skill_offer = skill_offer.lower()
    self.skill_want = skill_want.lower()

class SkillMatcher:
  def __init__(self):
    self.users = []

  def add_user(self, user):
    self.users.append(user)

  def find_matches(self, current_user):
    matches = []
    for user in self.users:
      if current_user == user:
        continue
      if(user.skill_offer == current_user.skill_want and
         user.skill_want == current_user.skill_offer):
         matches.append(user)
    return matches

if 'skill_matcher' not in st.session_state:
  st.session_state.skill_matcher = SkillMatcher()

if 'current_user' not in st.session_state:
  st.session_state.current_user = None

st.title("🤝 SkillSwap: Community Skill Exchange")
st.write("Exchange skills with others in your community!")


with st.form("user_form"):
  st.subheader("Enter Your Details")
  name = st.text_input("👤 Name")
  email = st.text_input("📧 Email")
  skill_offer = st.text_input("🛠️ I can teach..")
  skill_want = st.text_input("🔍 I want to learn..")
  submit_button = st.form_submit_button("Submit")

if submit_button and name and email and skill_offer and skill_want:
  new_user = User(name, email, skill_offer, skill_want)
  st.session_state.skill_matcher.add_user(new_user)
  st.session_state.current_user = new_user
  st.success(f"Welcome {name} you have joinded Skill Swap successfully!")

if st.session_state.current_user:
   matches=st.session_state.skill_matcher.find_matches(st.session_state.current_user)

   st.subheader("🔍 Potential Matches:")
   if matches:
     for match in matches:
       st.markdown(f"**{match.name}** can teach you **{match.skill_offer}** and you can learn **{match.skill_want}** **contact-email:{match.email}**")
   else:
     st.info("No potential matches found")

