## PyChain Ledger

## Overview

PyChain Ledger is a blockchain-based ledger system developed to facilitate financial transactions between partner banks. It allows users to create a decentralized ledger for recording transactions, ensuring data integrity and transparency. The project includes a user-friendly web interface built with Streamlit, enabling users to interact with the blockchain seamlessly.

## Features

- **Create Transaction Records:** Users can input transaction details including sender, receiver, and amount.
- **Blockchain Structure:** Each transaction is stored in a block, linked to the previous block, forming a secure chain.
- **Proof of Work:** Implements a proof-of-work consensus mechanism to validate new blocks.
- **Blockchain Validation:** Users can validate the entire blockchain to ensure data integrity.
- **User Interface:** Streamlit provides an interactive interface for adding transactions and viewing the blockchain.

## Installation

1. **Clone the Repository:** 
    
    `git clone <repository-url>`
    
2. **Install Dependencies:**  
    Ensure you have Python installed, then install the required packages:bash
    
    `pip install -r requirements.txt`
    
3. **Run the Application:**  
    Launch the Streamlit application:bash
    
    `streamlit run pychain.py`
    

## Usage

1. **Add a Block:**
    
    - Enter the sender, receiver, and transaction amount in the provided input fields.
    - Click "Add Block" to mine a new block and add it to the blockchain.
    
2. **Inspect the Ledger:**
    
    - View the entire blockchain ledger in the main interface.
    - Use the sidebar to inspect individual blocks.
    
3. **Validate the Blockchain:**
    
    - Click "Validate Chain" to check the blockchain's integrity.
    - A message will indicate whether the blockchain is valid.
    

## Code Structure

- **`Record` Class:** Defines the structure for transaction records with attributes for sender, receiver, and amount.
- **`Block` Class:** Represents each block in the blockchain, storing a transaction record and linking to the previous block.
- **`PyChain` Class:** Manages the blockchain, including adding blocks and validating the chain.
- **Streamlit Interface:** Provides input fields and buttons for user interaction, displaying the blockchain and validation results.
