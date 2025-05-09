{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNz5IyX3KCt/5aNboyY0jRu",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/hammmad-03444/skillMatcher/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "m-8_U_i627FU",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0a716dff-9a66-41ca-ace4-66fe02ef14be"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🌍 Open this link to access your Streamlit app:\n",
            "NgrokTunnel: \"https://1360-34-86-30-67.ngrok-free.app\" -> \"http://localhost:8501\"\n"
          ]
        }
      ],
      "source": [
        "\n",
        "import streamlit as st\n",
        "\n",
        "class User:\n",
        "  def __init__(self, name, email, skill_offer, skill_want):\n",
        "    self.name = name\n",
        "    self.email = email\n",
        "    self.skill_offer = skill_offer.lower()\n",
        "    self.skill_want = skill_want.lower()\n",
        "\n",
        "class SkillMatcher:\n",
        "  def __init__(self):\n",
        "    self.users = []\n",
        "\n",
        "  def add_user(self, user):\n",
        "    self.users.append(user)\n",
        "\n",
        "  def find_matches(self, current_user):\n",
        "    matches = []\n",
        "    for user in self.users:\n",
        "      if current_user == user:\n",
        "        continue\n",
        "      if(user.skill_offer == current_user.skill_want and\n",
        "         user.skill_want == current_user.skill_offer):\n",
        "         matches.append(user)\n",
        "    return matches\n",
        "\n",
        "if 'skill_matcher' not in st.session_state:\n",
        "  st.session_state.skill_matcher = SkillMatcher()\n",
        "\n",
        "if 'current_user' not in st.session_state:\n",
        "  st.session_state.current_user = None\n",
        "\n",
        "st.title(\"🤝 SkillSwap: Community Skill Exchange\")\n",
        "st.write(\"Exchange skills with others in your community!\")\n",
        "\n",
        "\n",
        "with st.form(\"user_form\"):\n",
        "  st.subheader(\"Enter Your Details\")\n",
        "  name = st.text_input(\"👤 Name\")\n",
        "  email = st.text_input(\"📧 Email\")\n",
        "  skill_offer = st.text_input(\"🛠️ I can teach..\")\n",
        "  skill_want = st.text_input(\"🔍 I want to learn..\")\n",
        "  submit_button = st.form_submit_button(\"Submit\")\n",
        "\n",
        "if submit_button and name and email and skill_offer and skill_want:\n",
        "  new_user = User(name, email, skill_offer, skill_want)\n",
        "  st.session_state.skill_matcher.add_user(new_user)\n",
        "  st.session_state.current_user = new_user\n",
        "  st.success(f\"Welcome {name} you have joinded Skill Swap successfully!\")\n",
        "\n",
        "if st.session_state.current_user:\n",
        "  matches=st.session_state.skill_matcher.find_matches(st.session_state.current_user)\n",
        "\n",
        "st.subheader(\"🔍 Potential Matches:\")\n",
        "if matches:\n",
        "  for match in matches:\n",
        "    st.markdown(f\"**{match.name}** can teach you **{match.skill_offer}** and you can learn **{match.skill_want}**\")\n",
        "else:\n",
        "  st.info(\"No potential matches found\")\n",
        "\n",
        "\n"
      ]
    }
  ]
}
