# GenAI Course - Week 1 Assignment
# Streamlit Expense Tracker App
# Created by Krishnakumar - Vision Vibes (Team-2)


# 1️⃣ Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 2️⃣ Set page title
st.title("💰 Simple Expense Tracker")

# 3️⃣ Create a session-based DataFrame to store expenses temporarily
if "expenses" not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=["Category", "Amount"])

# 4️⃣ Input section - user enters category and amount
st.header("Add a new expense")

category = st.text_input("Enter category (e.g., Food, Travel, Rent):")
amount = st.number_input("Enter amount (₹)", min_value=0.0, step=10.0)

# Button to save entry
if st.button("➕ Add Expense"):
    if category and amount > 0:
        new_row = pd.DataFrame({"Category": [category], "Amount": [amount]})
        st.session_state.expenses = pd.concat([st.session_state.expenses, new_row], ignore_index=True)
        st.success(f"Added: {category} - ₹{amount}")
    else:
        st.warning("Please enter both category and amount.")

# 5️⃣ Show current expenses
st.header("📋 Current Expenses")
if not st.session_state.expenses.empty:
    st.dataframe(st.session_state.expenses)

    # 6️⃣ Show summary chart
    st.header("📊 Expense Summary by Category")
    summary = st.session_state.expenses.groupby("Category")["Amount"].sum()

    # Create a matplotlib chart
    fig, ax = plt.subplots()
    summary.plot(kind="bar", ax=ax)
    ax.set_ylabel("Total Amount (₹)")
    ax.set_xlabel("Category")
    ax.set_title("Expenses by Category")

    st.pyplot(fig)
else:
    st.info("No expenses added yet.")

# 7️⃣ Option to clear all data
if st.button("🗑️ Clear All"):
    st.session_state.expenses = pd.DataFrame(columns=["Category", "Amount"])
    st.info("All expenses cleared!")

# ✅ App ends here


