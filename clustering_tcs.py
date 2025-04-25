{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1039244c",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-25 23:26:27.524 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.290 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Diya\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-04-25 23:26:28.290 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.316 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.316 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.316 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.316 Session state does not function when running a script without `streamlit run`\n",
      "2025-04-25 23:26:28.324 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.324 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.327 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.329 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.367 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.512 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.512 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.536 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.668 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.668 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.702 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.849 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.851 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:28.884 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:29.047 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-25 23:26:29.047 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Load data\n",
    "st.title(\"Clustering Dashboard\")\n",
    "data = pd.read_csv(\"clustered.csv\")  # or generate it live\n",
    "\n",
    "# Sidebar options\n",
    "cluster_to_view = st.sidebar.selectbox(\"Select Cluster\", sorted(data['Cluster'].unique()))\n",
    "\n",
    "st.subheader(f\"Distribution of Categorical Features for Cluster {cluster_to_view}\")\n",
    "filtered_data = data[data['Cluster'] == cluster_to_view]\n",
    "\n",
    "# Plotting\n",
    "for col in ['Sex', 'Housing', 'Saving accounts', 'Checking account', 'Purpose', 'Job']:\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.countplot(x=col, data=filtered_data, ax=ax)\n",
    "    plt.xticks(rotation=45)\n",
    "    st.pyplot(fig)\n",
    "    \n",
    "st.subheader(\"Numerical Feature Distributions by Cluster\")\n",
    "\n",
    "numerical_features = ['Age', 'Credit amount', 'Duration']\n",
    "\n",
    "for feature in numerical_features:\n",
    "    fig, ax = plt.subplots(figsize=(8, 6))\n",
    "    sns.boxplot(x='Cluster', y=feature, data=df, palette='viridis', ax=ax)\n",
    "    ax.set_title(f'{feature} Distribution by Cluster')\n",
    "    ax.set_xlabel('Cluster')\n",
    "    ax.set_ylabel(feature)\n",
    "    st.pyplot(fig)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef25b52b",
   "metadata": {},
   "outputs": [],
   "source": [
    "!streamlit run app.py"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
