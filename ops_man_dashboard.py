# __________________________________________________________________________________________________

# Initialization
# ___________________________________________________________________________________________________

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import math

# __________________________________________________________________________________________________

# Dashboard Layout and Model Selection
# ___________________________________________________________________________________________________

st.set_page_config(
    page_title="MAN4504 Operations Strategy Dashboard",
    page_icon="📦",                  
    layout="wide",                    
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    /* Apply Times New Roman to everything */
    html, body, div, p, span, h1, h2, h3, h4, h5, h6, li, ul, ol, table, th, td, label, input, textarea {
        font-family: 'Times New Roman', Times, serif !important;
        color: #F5F5F5;
    }

    /* Background - UF dark navy */
    body {
        background-color: #0021A5;
    }

    /* Widget background - slightly lighter blue */
    .stApp {
        background-color: #0021A5;
    }

    /* Radio buttons and input fields */
    input, .stRadio > div {
        background-color: #FA4616 !important;
        color: white !important;
        border-radius: 8px;
        padding: 4px 10px;
    }

    /* Primary highlight: Gator orange */
    .st-bf, .st-c7, .st-ds {
        color: #FFFFFF !important;
    }

    /* Buttons */
    .stButton>button {
        background-color: #0021A5;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1.2em;
    }

    .stButton>button:hover {
        background-color: #d73a13;
        color: white;
    }

    /* Remove sidebar, header, and footer */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { background-color: 	#191970 !important;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 0.5, 1])

with col2:
    st.image("https://brandcenter.p01.wp.it.ufl.edu/wp-content/uploads/sites/57/2024/06/NEW-IMAGES_The-University-Seal_The-University-Seal-1-2-768x768-1.png", width=150)

st.markdown("<h2 style='text-align: center; '>MAN4504: Exam 3- Prep Dashboard</h2>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 16px;'>Welcome! This dashboard is an educational toolkit designed to strengthen your operations management skillset. It features three interactive models based on material from Chapter 12 (Inventory Management), Chapter 8 (Revenue Management), and Chapter 13 (Aggregate Planning). Each model includes detailed explanations, relevant formulas, visualizations, and interactive prompts that allow you to define key variables and simulate data-driven decision-making. The methodologies used are directly derived from course concepts and are intended to reinforce understanding through hands-on application.</p>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

left, center, right = st.columns([1, 30, 1])

with center:
    module = st.radio("Select Curriculum-Based Model:",
        ["EOQ and Discount Quantity Model", "Newsvendor Model", "Aggregate Planning Model", "Critical Path Method, PERT Analysis, and Project Crashing"],
        horizontal=True
    )

st.markdown("<hr>", unsafe_allow_html=True)

# __________________________________________________________________________________________________

# Chapter 12: Inventory Management Module
# ___________________________________________________________________________________________________

if module == "EOQ and Discount Quantity Model":
    st.markdown("<h4 style='text-align: center; font-style: italic; '>Determining Optimal Order Policies</h4>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'>Proceed to the interactive prompts below to begin. Refer to the text boxes for detailed conceptual material. Relevant variables and formulas are explicitly defined throughout.</td>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    big_picture_question = st.selectbox(
         "What is any company's primary goal?",
         [
             "",  
             "To keep employees happy",
             "To maximize profit",
             "To reduce customer complaints",
             "To increase production output"
          ]
    )

    if big_picture_question:
        if big_picture_question == "To maximize profit":
            st.success("Correct! The primary goal of any company is to maximize profit.")
        else:
            st.error("Not quite. Try again!")

    st.markdown("<hr>", unsafe_allow_html=True)

    key_question = st.selectbox(
         "On a fundamental level, inventory management helps operations managers decide how much inventory to order and when to order it. Consider your previous response and imagine you’re now tasked with adjusting the ordering policy at Company X. Which of the following factors would you consider?",
         [
             "",  
             "Potential revenue loss from demand exceeding production",
             "Potential cost incurred from producing more than what is demanded",
             "Lead time — the delay between placing and receiving inventory",
             "All of the above"
          ]
    )

    if key_question:
        if key_question == "All of the above":
            st.success("Correct! All of these factors should be taken into consideration.")
        else:
            st.error("Not quite. Try again!")

    st.markdown("<hr>", unsafe_allow_html=True)

    broad_perspective_question = st.selectbox(
         "Therefore, what is the fundamental objective of inventory management?",
         [
             "",  
             "To balance tradeoffs between production and HR constraints",
             "To fulfill every customer order, regardless of cost",
             "To maximize revenue from demand while minimizing inventory-related costs",
             "To order as infrequently as possible to save money"
          ]
    )

    if broad_perspective_question:
        if broad_perspective_question == "To maximize revenue from demand while minimizing inventory-related costs":
            st.success("Correct! That’s the core purpose of inventory management. In practice, this typically involves balancing cost and demand since we rarely have perfect information about future demand or lead times.")
        else:
            st.error("Not quite. Try again!")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'>Chapter 12 centers around driving this objective through formulaic decision-making models: the Economic Order Quantity (EOQ) Model, Quantity Discount Model, Production Order Quantity (POQ) Model, and safety stock-related probabalistic models.</td>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'>In the Economic Order Quantity (EOQ) Model, calculations are based on these core variables:</td>", unsafe_allow_html=True)

    st.latex("Q = \\text{Quantity ordered}")
    st.latex("H = \\text{Holding cost per unit per year}")
    st.latex("D = \\text{Annual demand}")
    st.latex("S = \\text{Setup cost per order}")
    st.latex("d = \\text{Daily demand}")
    st.latex("L = \\text{Lead time in days}")
    st.latex("n = \\text{Number of working days}")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'>The EOQ Model assumes constant demand & lead time across time periods, instanteous replenishment, and fixed purchase prices (no discounts). It further assumes that demand is consistently met and therefore, quantity ordered (Q) can be set equal to Economic Order Quantity. The following formula should be used to determine EOQ:</td>", unsafe_allow_html=True)
         
    st.latex(r"Q^* = \sqrt{\frac{2DS}{H}}")

    st.markdown("<td style='text-align: center; font-size: 16px;'>Annual demand (D) and holding cost (H) are assumed to be known.</td>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'>After you calculate the EOQ, you can plug the value into Q and use the following formulas to determine annual costs:</td>", unsafe_allow_html=True)

    st.latex(r"\text{Annual inventory holding cost} = \frac{Q}{2}H")
    st.latex(r"\text{Annual setup cost} = \frac{D}{Q}S")
    st.latex(r"\text{Total cost} = \frac{Q}{2}H + \frac{D}{Q}S + PD")

    st.markdown("<td style='text-align: center; font-size: 16px;'>Annual inventory holding cost is calculated by multiplying holding cost per year (H) by average inventory level (Q/2). Annual setup cost is calculated by multiplying setup cost per order (S) by the number of annual orders (D/Q). Total cost is the sum total of annual inventory holding cost, annual setup cost, and purchase price (P) multiplied by demand.</td>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'>Adjust annual demand, holding cost, and setup cost with the toggles below to calculate EOQ and total annual cost. </td>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    left, right = st.columns([1, 1])
    with left:
        D = st.number_input("Demand (D) in units / year:", min_value=0.00, step=1.00)
    with right:
        H = st.number_input("Holding Cost (H) in $ / unit:", min_value=0.00, step=0.01)

    left, right = st.columns([1, 1])
    with left:
        S = st.number_input("Setup Cost (S) in $ / order:", min_value=0.0, step=0.01)
    with right:
        P = st.number_input("Purchase Price (P) in $ / unit:", min_value=0.0, step=0.01)

    st.markdown("<hr>", unsafe_allow_html=True)

    if st.button("Calculate EOQ & Total Cost"):
        if D > 0 and H > 0 and S > 0:
            EOQ = (2 * D * S / H) ** 0.5
        
            annual_holding_cost = (EOQ / 2) * H
        
            annual_setup_cost = (D / EOQ) * S
        
            total_cost = annual_holding_cost + annual_setup_cost + P * D

            st.success(f"**Economic Order Quantity (EOQ)**: {EOQ:.2f} units")
            st.success(f"**Total Annual Cost**: ${total_cost:,.2f}")

            st.markdown("<hr>", unsafe_allow_html=True)

            st.latex(rf"Q^* = \sqrt{{\frac{{2 \cdot {D:.0f} \cdot {S:.0f}}}{{{H:.0f}}}}} = {EOQ:.2f}")

            st.latex(rf"\text{{Annual Holding Cost}} = \frac{{{EOQ:.2f}}}{{2}} \cdot {H:.0f} = {annual_holding_cost:,.2f}")

            st.latex(rf"\text{{Annual Setup Cost}} = \frac{{{D:.0f}}}{{{EOQ:.2f}}} \cdot {S:.0f} = {annual_setup_cost:,.2f}")

            st.latex(rf"\text{{Total Cost}} = {annual_holding_cost:,.2f} + {annual_setup_cost:,.2f} + {P:.0f} \cdot {D:.0f} = {total_cost:,.2f}") 

            st.markdown("<br>", unsafe_allow_html=True)           

            labels = ['Annual Holding Cost', 'Annual Setup Cost']
            values = [annual_holding_cost, annual_setup_cost]

            fig, ax = plt.subplots()
            ax.set_title('Annual Cost of Ordering & Holding Inventory: Breakdown', fontsize=14, fontweight='bold', color='white', pad=20)
            fig.patch.set_facecolor('#B22222')	
            ax.set_facecolor('#0021A5')
            bars = ax.bar(labels, values, color=['#B22222', '#B22222'])
            ax.tick_params(axis='x', colors='white', labelsize=8)
            ax.tick_params(axis='y', colors='white', labelsize=8)
            max_value = max(values)
            ax.set_ylim(0, max_value * 1.25)
            ax.margins(x=0.1)
            ax.set_ylabel(
                'Cost ($)',
                fontsize=12,
                fontweight='bold',
                color='white',
                labelpad=15  
            )
            ax.set_xlabel(
                'Cost Components',
                fontsize=12,
                fontweight='bold',
                color='white',
                labelpad=15  
            )
            for bar in bars:
                height = bar.get_height()
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    height,
                    f"${height:,.2f}",
                    ha='center',
                    va='bottom',
                    fontsize=10,
                    fontweight='bold',
                    color='white'
            )

            st.pyplot(fig)

            st.info(f"""
            To minimize total cost, you should order approximately **{EOQ:.0f} units per order**.  
            This balances your setup cost (**\\${S:.2f}**) and holding cost (**\\${H:.2f}** per unit/year).  

            The total annual cost includes:
            - **Holding Cost** = ${annual_holding_cost:,.2f}  
            - **Setup Cost** = ${annual_setup_cost:,.2f}  
            - **Purchasing Cost** = ${P:.2f} × {D:.0f} = ${P * D:,.2f}
            """)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'>Use the toggles next to each variable to answer the following questions about input-output relationships:</td>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)           

    relationship_question1 = st.selectbox(
         "Which of the following statements accurately represent the relationship between demand and Economic Order Quantity?",
         [
             "",  
             "Proportional",
             "Inverse",
             "Demand has no effect on Economic Order Quantity",
          ]
    )

    if relationship_question1:
        if relationship_question1 == "Proportional":
            st.success("Correct! As demand increases, EOQ increases. As demand decreases, EOQ decreases.")
        else:
            st.error("Not quite. Try again!")

    relationship_question2 = st.selectbox(
         "Which of the following statements accurately represents the relationship between demand and total annual cost?",
         [
             "",  
             "Proportional",
             "Inverse",
             "Demand has no effect on total annual cost",
          ]
    )

    if relationship_question2:
        if relationship_question2 == "Proportional":
            st.success("Correct! As demand increases, total annual cost increases. As demand decreases, total annual cost decreases.")
        else:
            st.error("Not quite. Try again!")

    relationship_question3 = st.selectbox(
         "Which of the following statements accurately represents the relationship between holding cost and Economic Order Quantity?",
         [
             "",  
             "Proportional",
             "Inverse",
             "Holding cost has no effect on total annual cost",
          ]
    )

    if relationship_question3:
        if relationship_question3 == "Inverse":
            st.success("Correct! As holding cost increases, Economic Order Quantity decreases. As holding cost decreases, Economic Order Quantity increases.")
        else:
            st.error("Not quite. Try again!")

    relationship_question4 = st.selectbox(
         "Which of the following statements accurately represents the relationship between setup cost and Economic Order Quantity?",
         [
             "",  
             "Proportional",
             "Inverse",
             "Setup cost has no effect on total annual cost",
          ]
    )

    if relationship_question4:
        if relationship_question4 == "Proportional":
            st.success("Correct! As setup cost increases, Economic Order Quantity increases. As setup cost decreases, Economic Order Quantity decreases.")
        else:
            st.error("Not quite. Try again!")

    relationship_question5 = st.selectbox(
         "Which of the following statements accurately represents the relationship between purchase price and Economic Order Quantity?",
         [
             "",  
             "Proportional",
             "Inverse",
             "Purchase price has no effect on Economic Order Quantity",
          ]
    )

    if relationship_question5:
        if relationship_question5 == "Purchase price has no effect on Economic Order Quantity":
            st.success("Correct! Purchase price is not part of the calculation for Economic Order Quantity.")
        else:
            st.error("Not quite. Try again!")

    st.markdown("<td style='text-align: center; font-size: 16px;'>Refer to the bar chart to answer the following question about cost relationships:</td>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    relationship_question6 = st.selectbox(
         "Which of the following statements accurately represents the relationship between annual inventory holding cost and annual setup cost?",
         [
             "",  
             "Proportional",
             "Inverse",
             "Annual holding cost and annual setup cost are not correlated",
             "Annual holding cost is always equal to annual setup cost",
          ]
    )

    if relationship_question6:
        if relationship_question6 == "Annual holding cost is always equal to annual setup cost":
            st.success("Correct! In the Economic Order Quantity Model, annual inventory holding cost and annual setup cost are always equal.")
        else:
            st.error("Not quite. Try again!")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'>Proceed to the interactive prompts below to learn about the Quantity Discount Model.</td>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    qd_intro_q1 = st.selectbox(
        "Imagine you're buying inventory for your business. Why might you choose to order a larger quantity than usual?",
        [
            "",
            "To take advantage of lower prices per unit",
            "To avoid dealing with the supplier again later",
            "To make inventory management easier",
            "To increase storage costs"
        ]
    )

    if qd_intro_q1:
        if qd_intro_q1 == "To take advantage of lower prices per unit":
            st.success("Correct! Many suppliers offer lower prices for larger orders. This is known as a quantity discount.")
        else:
            st.error("Not quite. Try again!")


    qd_intro_q2 = st.selectbox(
        "If ordering more means a lower price per unit, why might a business *not* always take that option?",
        [
            "",
            "Because larger orders come with higher holding costs",
            "Because customers might get suspicious",
            "Because prices may increase again later",
            "Because it’s illegal to buy in bulk"
        ]
    )

    if qd_intro_q2:
        if qd_intro_q2 == "Because larger orders come with higher holding costs":
            st.success("Correct! Even if the unit price drops, the cost of storing extra inventory can increase total cost.")
        else:
            st.error("Not quite. Try again!")

        st.markdown("<hr>", unsafe_allow_html=True)

    qd_intro_q3 = st.selectbox(
        "As a buyer, what is your goal when deciding how much to order under a quantity discount?",
        [
            "",
            "To minimize the price per unit",
            "To minimize total cost, including purchase, setup, and holding costs",
            "To always buy the most you can afford",
            "To avoid making multiple purchases"
        ]
    )

    if qd_intro_q3:
        if qd_intro_q3 == "To minimize total cost, including purchase, setup, and holding costs":
            st.success("Correct! The optimal decision is the one that minimizes *total* cost, not just purchase cost per unit.")
        else:
            st.error("Not quite. Try again!")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'>Each range of quantity purchased in the table below represents the Economic Order Quantity. The dashboard automatically simulates each range consisting of or exceeding the EOQ calculated from your current inputs:</td>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    data = {
        "Quantity Purchased": ["0–499", "500–999", "1000+"],
        "Price per Unit ($)": [5, 4.75, 4.5]
    }

    df = pd.DataFrame(data)
    df["Price per Unit ($)"] = df["Price per Unit ($)"].apply(lambda x: f"${x:.2f}")
    st.markdown("<h5 style='text-align: center;'>Quantity Discount Table</h5>", unsafe_allow_html=True)
    st.table(df) 
    
    discount_tiers = [
        {"min_qty": 0, "max_qty": 499, "price": 5.00},
        {"min_qty": 500, "max_qty": 999, "price": 4.75},
        {"min_qty": 1000, "max_qty": float("inf"), "price": 4.50}
    ]

    EOQ = None
    eoq_tier_index = None
    options = []

    if D > 0 and H > 0 and S > 0:

        # Calculate EOQ
        EOQ = (2 * D * S / H) ** 0.5

        # Determine which tier EOQ falls into
        for i, tier in enumerate(discount_tiers):
            if tier["min_qty"] <= EOQ <= tier["max_qty"]:
                eoq_tier_index = i
                break

        # If EOQ falls in a tier (safe), calculate total cost comparisons
        if eoq_tier_index is not None:
            base_price = discount_tiers[eoq_tier_index]["price"]
            purchase_cost = D * base_price
            setup_cost = (D / EOQ) * S
            holding_cost = (EOQ / 2) * H
            total_cost = purchase_cost + setup_cost + holding_cost

            options.append({
                "Order Quantity": EOQ,
                "Price per Unit ($)": f"${base_price:.2f}",
                "Total Annual Cost ($)": total_cost
            })

            # Evaluate all higher tiers
            for tier in discount_tiers[eoq_tier_index + 1:]:
                q = tier["min_qty"]
                p = tier["price"]
                purchase_cost = D * p
                setup_cost = (D / q) * S
                holding_cost = (q / 2) * H
                total_cost = purchase_cost + setup_cost + holding_cost

                options.append({
                    "Order Quantity": q,
                    "Price per Unit ($)": f"${p:.2f}",
                    "Total Annual Cost ($)": total_cost
                })

            # Display results
            df_compare = pd.DataFrame(options)
            best_option = df_compare.loc[df_compare["Total Annual Cost ($)"].idxmin()]

            st.markdown("Comparison of Quantity Discount Scenarios:")
            st.dataframe(df_compare.style.highlight_min(subset=["Total Annual Cost ($)"], color="#2ecc71"))

            st.success(f"Optimal Order Quantity: **{best_option['Order Quantity']:.0f} units** at **{best_option['Price per Unit ($)']}**")

    else:
        st.warning("Please enter positive values for demand, holding cost, and setup cost to perform this calculation.")

    st.markdown("<td style='text-align: center; font-size: 16px;'>If the calculated EOQ already meets the largest quantity threshold, you don't need to take any further steps; you already found the optimal order quantity after the discount. However, if your original EOQ falls under one of the first two quantity thresholds, total cost must be recalculated with EOQ being set equal to the lowest quantity within each range and using corresponding purchase prices. The quantity with the lowest total annual cost is the optimal order quantity. This process is illustrated by the calculation table above. If your calculation table currently only has one row and you'd like to see the Quantity Discount Model in action, adjust your inputs to reduce the EOQ. Recall that decreasing demand, increasing holding costs, and decreasing setup costs are all effective methods of decreasing EOQ.</td>", unsafe_allow_html=True)

# __________________________________________________________________________________________________

# Chapter 8: Revenue Management
# ___________________________________________________________________________________________________

elif module == "Newsvendor Model":
    st.markdown("<h4 style='text-align: center; font-style: italic; '>The Critical Ratio & Newsvendor Model</h4>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'>Proceed to the interactive prompt below to begin. Refer to the text boxes for detailed conceptual material. Relevant variables and formulas are explicitly defined throughout.</td>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    revenue_q2 = st.selectbox(
        "If you produce too many flowers and they go unsold, what happens? If you produce too few and run out, what happens?",
        [
            "",
            "Both scenarios are equally costly and should be avoided entirely",
            "Too many results in waste and too few results in missed sales; both have different costs",
            "Producing too many is worse because it wastes money",
            "Producing too few is worse because customers get upset"
        ]
    )

    if revenue_q2:
        if revenue_q2 == "Too many results in waste and too few results in missed sales; both have different costs":
            st.success("Correct! The core idea of revenue management is that overestimating and underestimating demand each have their own unique costs and should be weighed carefully.")
        else:
            st.error("Not quite. Try again!")


    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'>Chapter 8 is centered around revenue management, also known as yield management. It is used to maximize revenue through changes in pricing. The Newsvendor Model model determines how many units to supply when a company must weigh the cost of over-predicting or under-predicting damand using the Critical Ratio. It is used for products that perish or lose relevance within an incredibly short time frame, like milk or newspapers.</td>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'> Newsvendor Model calculations are based on these core variables:</td>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.latex(r"c_u = \text{cost of unmet demand}")
    st.latex(r"c_o = \text{cost of overage}")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'>The Critical Ratio is the probability by which such a company should over-predict demand. Relevant formulas are as follows:</td>", unsafe_allow_html=True)

    st.latex(r"c_u = \text{sales price} - \text{purchase price}")
    st.latex(r"c_o = \text{purchase price} - \text{salvage value}")
    st.latex(r"CR = \frac{c_u}{c_o + c_u}")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'>Adjust sales price, purchase price, and salvage value below to calculate the critical ratio.</td>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    left, center, right = st.columns([1, 1, 1])
    with left:
        SP = st.number_input("Sales price in $:", min_value=0.00, step=0.01)
    with center:
        PP = st.number_input("Purchase price in $:", min_value=0.00, step=0.01)
    with right:
        SV = st.number_input("Salvage value in $:", min_value=0.00, step=0.01)

    st.markdown("<td style='text-align: center; font-size: 16px;'>Salvage value refers to any money that can be recovered from unsold units. With perishables, this might be through discounted clearance sales (if the item has not expired), secondary markets, donations with tax write-offs, etc. For products that lose value immediately like newspapers, salvage value is generally assumed to be zero. This makes the cost of overage very high.</td>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Calculate Critical Ratio"):
        if SP > PP:
            cu = SP - PP
            co = PP - SV

            if cu + co > 0:
                CR = cu / (cu + co)

                st.success(f"**Critical Ratio (CR):** {CR:.4f}")

                st.markdown("<hr>", unsafe_allow_html=True)

                st.latex(rf"c_u = {SP:.2f} - {PP:.2f} = {cu:.2f}")
                st.latex(rf"c_o = {PP:.2f} - {SV:.2f} = {co:.2f}")
                st.latex(rf"CR = \frac{{{cu:.2f}}}{{{cu:.2f} + {co:.2f}}} = {CR:.4f}")
            else:
                st.error("Invalid input: Denominator (c_u + c_o) must be greater than 0.")
        else:
            st.error("Sales price must be greater than purchase price to calculate unmet demand cost (c_u).")

    st.markdown("<hr>", unsafe_allow_html=True)

    relationship_question7 = st.selectbox(
         "Which of the following statements accurately represents the relationship between sales price and the Critical Ratio?",
         [
             "",  
             "Proportional",
             "Inverse",
             "An inverted U-Pattern (Critical ratio increases until a specific input value then declines)",
          ]
    )

    if relationship_question7:
        if relationship_question7 == "Proportional":
            st.success("Correct! As sales price increases, the Critical Ratio increases. As sales price decreases, the Critical Ratio decreases.")
        else:
            st.error("Not quite. Try again!")

    relationship_question8 = st.selectbox(
         "Which of the following statements accurately represents the relationship between purchase price and the Critical Ratio?",
         [
             "",  
             "Proportional",
             "Inverse",
             "An inverted U-Pattern (Critical ratio increases until a specific input value then declines)",
          ]
    )

    if relationship_question8:
        if relationship_question8 == "An inverted U-Pattern (Critical ratio increases until a specific input value then declines)":
            st.success("Correct! As purchase price increases, the Critical Ratio increases until a specific purchase price is reached, then declines.")
        else:
            st.error("Not quite. Try again!")

    relationship_question9 = st.selectbox(
         "Which of the following statements accurately represents the relationship between salvage value and the Critical Ratio?",
         [
             "",  
             "Proportional",
             "Inverse",
             "An inverted U-Pattern (Critical ratio increases until a specific input value then declines)",
          ]
    )

    if relationship_question9:
        if relationship_question9 == "Proportional":
            st.success("Correct! As salvage value increases, the Critical Ratio increases. As salvage value decreases, the Critical Ratio decreases.")
        else:
            st.error("Not quite. Try again!")

    st.markdown("<td style='text-align: center; font-size: 16px;'>Once the Critical Ratio is calculated, use a z-table to find the z-score associated with that probability.</td>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    CR_z_input = st.number_input("Enter Critical Ratio (CR) value:", min_value=0.0, max_value=1.0, step=0.01)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'>This z-score tells you how many standard deviations above the mean the optimal order quantity should be.</td>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    if CR_z_input > 0 and CR_z_input < 1:
        from scipy.stats import norm
        z_value = norm.ppf(CR_z_input)
        st.success(f"Z-score associated with CR {CR_z_input:.2f}: {z_value:.2f}")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<td style='text-align: center; font-size: 16px;'>Input assumptions for mean and standard deviation of demand to determine optimal order quantity.</td>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    mu = st.number_input("Mean demand (μ):", min_value=0.0, step=1.0)
    sigma = st.number_input("Standard deviation (σ):", min_value=0.0, step=0.1)

    if mu > 0 and sigma > 0 and CR_z_input > 0 and CR_z_input < 1:
        Q_star = mu + z_value * sigma
        st.success(f"Optimal Order Quantity (Q*): {Q_star:.2f} units")
        st.latex(rf"Q^* = {mu:.2f} + {z_value:.2f} \cdot {sigma:.2f} = {Q_star:.2f}")

# __________________________________________________________________________________________________

# Chapter 13: Aggregate Planning
# ___________________________________________________________________________________________________

elif module == "Aggregate Planning Model":
    st.markdown("<h4 style='text-align: center; font-style: italic;'>Chase vs. Level: Strategy Blending with the Aggregate Planning Model</h4>", unsafe_allow_html=True)

    agg_q1 = st.selectbox(
        "Imagine you're managing a business. Which of the following goals best captures your mindset when planning for the next year?",
        [
            "",
            "Make detailed daily staffing schedules",
            "Ensure production exactly matches customer demand every day",
            "Create a cost-effective strategy to meet expected demand over time",
            "Focus solely on short-term cash flow"
        ]
    )

    if agg_q1:
        if agg_q1 == "Create a cost-effective strategy to meet expected demand over time":
            st.success("Correct! This aligns with the mindset behind mid-range operations planning.")
        else:
            st.error("Not quite. Try again!")

    agg_q2 = st.selectbox(
        "Why might it be unrealistic for a company to schedule production and staffing decisions week-by-week for an entire year?",
        [
            "",
            "Because employees don’t like rigid schedules",
            "Because long-term demand is uncertain and planning every week would be inefficient",
            "Because raw materials are usually unavailable for that long",
            "Because government regulations require quarterly changes"
        ]
    )

    if agg_q2:
        if agg_q2 == "Because long-term demand is uncertain and planning every week would be inefficient":
            st.success("Correct! It’s more practical to make broader plans that can be adjusted later.")
        else:
            st.error("Not quite. Try again!")

    agg_q3 = st.selectbox(
        "You’re running a company and receive a 6-month forecast showing fluctuating customer demand. What’s your biggest operational challenge?",
        [
            "",
            "Keeping investors informed about long-term changes",
            "Maximizing employee happiness",
            "Determining how to adjust production or staffing to meet demand without overspending",
            "Tracking daily inventory levels"
        ]
    )

    if agg_q3:
        if agg_q3 == "Determining how to adjust production or staffing to meet demand without overspending":
            st.success("Correct! This is the core problem aggregate planning is meant to solve.")
        else:
            st.error("Not quite. Try again!")

    agg_q4 = st.selectbox(
        "What tradeoff do businesses typically face when deciding between keeping a steady workforce vs. adjusting it monthly?",
        [
            "",
            "Job satisfaction vs. health benefits",
            "Stability vs. responsiveness to demand",
            "Technology cost vs. advertising budget",
            "None — there's no tradeoff involved"
        ]
    )

    if agg_q4:
        if agg_q4 == "Stability vs. responsiveness to demand":
            st.success("Correct! That’s the essence of choosing between level and chase strategies.")
        else:
            st.error("Not quite. Try again!")
    agg_q5 = st.selectbox(
        "In reality, most businesses use a blend of different planning strategies. Why?",
        [
            "",
            "Because textbook strategies are illegal",
            "Because each strategy has pros and cons that depend on the company’s goals, costs, and workforce",
            "Because software forces them to",
            "Because only subcontractors can handle long-term demand"
        ]
    )

    if agg_q5:
        if agg_q5 == "Because each strategy has pros and cons that depend on the company’s goals, costs, and workforce":
            st.success("Correct! Mixed strategies allow businesses to adapt while managing cost and flexibility.")
        else:
            st.error("Not quite. Try again!")


    st.markdown("<td style='text-align: center; font-size: 16px;'>Aggregate planning is a mid-range production planning technique, generally focused on a range of 3 to 18 months. The goal is to meet demand while minimizing cost. Two common strategies are:</td>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("**Level Strategy** – Keep workforce constant, use inventory to meet demand.")
    st.markdown("**Chase Strategy** – Change workforce monthly to match demand exactly.")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("#### Core Costs to Minimize:")
    st.markdown("- **Inventory Holding Cost**: Cost to carry leftover units to the next month.")
    st.markdown("- **Hiring Cost**: Cost to bring in a new worker.")
    st.markdown("- **Firing Cost**: Cost to lay off a worker.")

    st.markdown("#### Key Formulas:")

    st.latex(r"\text{Workers Needed} = \left\lceil \frac{\text{Demand}}{\text{Units per Worker}} \right\rceil")
    st.latex(r"\text{Hired} = \max(0, \text{Workers Needed} - \text{Previous Workers})")
    st.latex(r"\text{Fired} = \max(0, \text{Previous Workers} - \text{Workers Needed})")
    st.latex(r"\text{Inventory} = \text{Previous Inventory} + \text{Production} - \text{Demand}")
    st.latex(r"\text{Total Cost} = \text{Hiring Cost} + \text{Firing Cost} + \text{Inventory Holding Cost}")

    st.markdown("<hr>", unsafe_allow_html=True)

    strategy = st.selectbox("Choose a Strategy to Simulate:", ["Chase Strategy", "Level Strategy"])

    demand = st.text_input("Enter monthly demand separated by commas (e.g., 1000,1200,900,1100):")
    if demand:
        try:
            forecast = [int(x.strip()) for x in demand.split(",")]
        except:
            st.error("Invalid input. Please enter only integers separated by commas.")

    units_per_worker = st.number_input("Units produced per worker per month:", min_value=1, step=1)
    initial_workers = st.number_input("Initial number of workers:", min_value=0, step=1)
    hire_cost = st.number_input("Hiring cost per worker:", min_value=0.0, step=10.0)
    fire_cost = st.number_input("Firing cost per worker:", min_value=0.0, step=10.0)
    hold_cost = st.number_input("Inventory holding cost per unit per month:", min_value=0.0, step=1.0)

    prod_rate = 0
    if strategy == "Level Strategy":
        prod_rate = st.number_input("Monthly production rate (Level Strategy):", min_value=0, step=1)

    if st.button("Run Aggregate Plan Calculation") and demand:
        import math
        results = []
        inventory = 0
        workers = initial_workers
        total_hiring = 0
        total_firing = 0
        total_inventory_cost = 0

        for month in range(len(forecast)):
            if strategy == "Chase Strategy":
                required_workers = math.ceil(forecast[month] / units_per_worker)
                hired = max(0, required_workers - workers)
                fired = max(0, workers - required_workers)
                prod_capacity = required_workers * units_per_worker
                workers = required_workers
            else:  # Level Strategy
                prod_capacity = prod_rate
                hired = 0
                fired = 0

            net_inventory = inventory + prod_capacity - forecast[month]
            inventory = max(0, net_inventory)
            inv_cost = inventory * hold_cost

            total_inventory_cost += inv_cost
            total_hiring += hired
            total_firing += fired

            results.append({
                "Month": month + 1,
                "Demand": forecast[month],
                "Production": prod_capacity,
                "Inventory": inventory,
                "Hired": hired,
                "Fired": fired,
                "Inventory Cost": inv_cost
            })

        total_hiring_cost = total_hiring * hire_cost
        total_firing_cost = total_firing * fire_cost
        total_cost = total_hiring_cost + total_firing_cost + total_inventory_cost

        st.dataframe(pd.DataFrame(results))

        st.markdown("<hr>", unsafe_allow_html=True)
        st.success(f"Total Hiring Cost: ${total_hiring_cost:,.2f}")
        st.success(f"Total Firing Cost: ${total_firing_cost:,.2f}")
        st.success(f"Total Inventory Cost: ${total_inventory_cost:,.2f}")
        st.markdown(f"**Total Cost: ${total_cost:,.2f}**")

    st.markdown("<hr>", unsafe_allow_html=True)

    relationship_question10 = st.selectbox(
         "Which of the following statements accurately represents the relationship between monthly demand and the number of workers needed under a Chase strategy?",
         [
             "",  
             "Proportional",
             "Inverse",
             "An inverted U-Pattern (Workers increase until a specific demand then decline)",
          ]
    )

    if relationship_question10:
        if relationship_question10 == "Proportional":
            st.success("Correct! As monthly demand increases, the number of workers needed under a Chase strategy increases.")
        else:
            st.error("Not quite. Try again!")

    relationship_question11 = st.selectbox(
         "Which of the following statements accurately represents the relationship between production and inventory level?",
         [
             "",  
             "Proportional",
             "Inverse",
             "An inverted U-Pattern (Inventory builds until a point then falls)",
          ]
    )

    if relationship_question11:
        if relationship_question11 == "Proportional":
            st.success("Correct! As production increases (relative to demand), inventory increases.")
        else:
            st.error("Not quite. Try again!")

    relationship_question12 = st.selectbox(
         "Which of the following statements accurately represents the relationship between holding cost per unit and total cost under a Level strategy?",
         [
             "",  
             "Proportional",
             "Inverse",
             "An inverted U-Pattern (Cost increases until a point then declines)",
          ]
    )

    if relationship_question12:
        if relationship_question12 == "Proportional":
            st.success("Correct! As holding cost per unit increases, total cost under a Level strategy increases.")
        else:
            st.error("Not quite. Try again!")

    relationship_question13 = st.selectbox(
         "Which of the following statements accurately represents the relationship between firing cost per worker and total cost under a Chase strategy?",
         [
             "",  
             "Proportional",
             "Inverse",
             "An inverted U-Pattern (Total cost rises then falls with firing cost)",
          ]
    )

    if relationship_question13:
        if relationship_question13 == "Proportional":
            st.success("Correct! As firing cost per worker increases, the total cost under a Chase strategy increases.")
        else:
            st.error("Not quite. Try again!")

    relationship_question14 = st.selectbox(
         "Which of the following statements accurately represents the relationship between initial workers and the number of workers hired in the first month under a Chase strategy?",
         [
             "",  
             "Proportional",
             "Inverse",
             "An inverted U-Pattern (Hired workers rise then fall based on staffing)",
          ]
    )

    if relationship_question14:
        if relationship_question14 == "Inverse":
            st.success("Correct! As initial workers increase, the number of workers hired in month one decreases.")
        else:
            st.error("Not quite. Try again!")

# __________________________________________________________________________________________________

# Chapter 3: Project Management
# ___________________________________________________________________________________________________

elif module == "Critical Path Method, PERT Analysis, and Project Crashing":
    st.markdown("<h4 style='text-align: center; font-style: italic;'>Planning, Prioritization, and Tradeoffs in Project Management</h4>", unsafe_allow_html=True)

    proj_q1 = st.selectbox(
        "Imagine you're leading a team to launch a new product in 6 months. What’s the first thing you should figure out?",
        [
            "",
            "How many people you’ll need for marketing",
            "What tasks need to be completed and how long they’ll take",
            "What competitor products are launching next year",
            "How much profit the product will make"
        ]
    )

    if proj_q1:
        if proj_q1 == "What tasks need to be completed and how long they’ll take":
            st.success("Correct! Project management starts by breaking down work into tasks and estimating their durations.")
        else:
            st.error("Not quite. Try again!")

    proj_q2 = st.selectbox(
        "You’re mapping out a multi-step project. Some steps can happen at the same time, while others must be completed first. Why does this matter?",
        [
            "",
            "It affects which tasks get assigned to senior managers",
            "It determines how quickly the project can finish overall",
            "It’s required by most accounting software",
            "It affects only the HR department’s approval timeline"
        ]
    )

    if proj_q2:
        if proj_q2 == "It determines how quickly the project can finish overall":
            st.success("Correct! Task sequencing determines which tasks are on the critical path; those which control total project time.")
        else:
            st.error("Not quite. Try again!")

    proj_q3 = st.selectbox(
        "Let’s say some tasks take longer than expected. What’s the most important reason to track task progress throughout the project?",
        [
            "",
            "To punish slow employees",
            "To provide updates to the marketing team",
            "To see if delays will affect the final project deadline",
            "To change team lunch breaks"
        ]
    )

    if proj_q3:
        if proj_q3 == "To see if delays will affect the final project deadline":
            st.success("Correct! Monitoring delays helps you react quickly, especially if they affect critical path activities.")
        else:
            st.error("Not quite. Try again!")

    proj_q4 = st.selectbox(
        "You’re under pressure to launch sooner than planned. What’s the most logical way to reduce the total project time?",
        [
            "",
            "Add more people to every team",
            "Start every task earlier",
            "Shorten the longest, most time-sensitive tasks (if possible)",
            "Cancel all non-critical tasks"
        ]
    )

    if proj_q4:
        if proj_q4 == "Shorten the longest, most time-sensitive tasks (if possible)":
            st.success("Correct! This is the core principle behind project crashing; targeting critical path tasks to reduce duration.")
        else:
            st.error("Not quite. Try again!")

    proj_q5 = st.selectbox(
        "Why don’t companies always crash their projects to finish as early as possible?",
        [
            "",
            "Because crashing is illegal in most states",
            "Because shortening tasks often comes with added cost or tradeoffs",
            "Because employees prefer long timelines",
            "Because early delivery always leads to quality problems"
        ]
    )

    if proj_q5:
        if proj_q5 == "Because shortening tasks often comes with added cost or tradeoffs":
            st.success("Correct! Crashing decisions involve balancing speed against cost; you only crash when it’s worth the tradeoff.")
        else:
            st.error("Not quite. Try again!")


    st.markdown("<td style='text-align: center; font-size: 16px;'>Project Management techniques help businesses plan, track, and optimize project timelines. Critical Path Method (CPM) and Program Evaluation Review Technique (PERT) are two major tools for managing complex, time-sensitive projects.</td>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("**Critical Path Method (CPM)** – Identifies the longest path of dependent tasks, setting the minimum project duration.")
    st.markdown("**PERT Analysis** – Incorporates uncertainty by using 3 estimates: Optimistic (O), Most Likely (M), and Pessimistic (P).")
    st.markdown("**Crashing** – Adds resources (usually at a cost) to shorten project time, starting with tasks on the critical path.")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("#### Key Formulas:")
    st.latex(r"\text{Expected Time (TE)} = \frac{O + 4M + P}{6}")
    st.latex(r"\text{Variance} = \left(\frac{P - O}{6}\right)^2")
    st.latex(r"\text{Slack} = \text{Latest Start} - \text{Earliest Start}")
    st.latex(r"\text{Project Duration} = \sum \text{TE on Critical Path}")

    st.markdown("<hr>", unsafe_allow_html=True)

    # Simulation Inputs
    st.markdown("Enter sample activity estimates below to calculate PERT values:")

    activity_label = st.text_input("Activity Name (e.g., A, B, C):")
    optimistic = st.number_input("Optimistic Time (O):", min_value=0.0, step=1.0)
    most_likely = st.number_input("Most Likely Time (M):", min_value=0.0, step=1.0)
    pessimistic = st.number_input("Pessimistic Time (P):", min_value=0.0, step=1.0)

    if st.button("Calculate PERT Estimates") and activity_label:
        TE = (optimistic + 4 * most_likely + pessimistic) / 6
        variance = ((pessimistic - optimistic) / 6) ** 2

        st.success(f"Expected Time (TE) for Activity {activity_label}: {TE:.2f}")
        st.success(f"Variance for Activity {activity_label}: {variance:.4f}")

    st.markdown("<hr>", unsafe_allow_html=True)

    # Relationship Questions
    relationship_question1 = st.selectbox(
         "Which of the following statements accurately represents the relationship between a task's time estimates and its expected time using PERT?",
         [
             "",
             "Proportional",
             "Inverse",
             "Weighted average of all estimates (heavily weighted toward most likely)",
          ]
    )

    if relationship_question1:
        if relationship_question1 == "Weighted average of all estimates (heavily weighted toward most likely)":
            st.success("Correct! The PERT formula weights the most likely time 4 times more than the others.")
        else:
            st.error("Not quite. Try again!")

    relationship_question2 = st.selectbox(
         "Which of the following statements accurately describes the relationship between a task’s slack and its inclusion on the critical path?",
         [
             "",
             "Proportional",
             "Inverse",
             "Zero slack tasks are always on the critical path",
          ]
    )

    if relationship_question2:
        if relationship_question2 == "Zero slack tasks are always on the critical path":
            st.success("Correct! Tasks with zero slack determine the project's minimum time.")
        else:
            st.error("Not quite. Try again!")

    relationship_question3 = st.selectbox(
         "Which of the following statements accurately reflects the relationship between crashing cost and project duration?",
         [
             "",
             "Proportional",
             "Inverse",
             "An inverted U-pattern (cost decreases then increases)",
          ]
    )

    if relationship_question3:
        if relationship_question3 == "Inverse":
            st.success("Correct! As you crash tasks (at increasing cost), total project duration decreases.")
        else:
            st.error("Not quite. Try again!")

    relationship_question4 = st.selectbox(
         "Which of the following statements accurately describes the relationship between variance and project duration risk?",
         [
             "",
             "Proportional",
             "Inverse",
             "Unrelated",
          ]
    )

    if relationship_question4:
        if relationship_question4 == "Proportional":
            st.success("Correct! As variance increases, the uncertainty around the project timeline also increases.")
        else:
            st.error("Not quite. Try again!")

    relationship_question5 = st.selectbox(
         "Which of the following statements accurately reflects the effect of crashing a non-critical task?",
         [
             "",
             "It shortens the project duration",
             "It increases project cost without changing total time",
             "It improves employee morale",
          ]
    )

    if relationship_question5:
        if relationship_question5 == "It increases project cost without changing total time":
            st.success("Correct! Crashing non-critical tasks wastes resources without reducing the timeline.")
        else:
            st.error("Not quite. Try again!")
