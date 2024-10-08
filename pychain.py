# PyChain Ledger

################################################################################

# Imports

import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib

################################################################################

# Step 1: Create a Record Data Class

@dataclass
class Record:
    sender: str
    receiver: str
    amount: float

################################################################################

# Step 2: Modify the Existing Block Data Class to Store Record Data

@dataclass
class Block:
    record: Record
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    nonce: int = 0

    def hash_block(self):
        sha = hashlib.sha256()
        record = str(self.record).encode()
        sha.update(record)
        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)
        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)
        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)
        nonce = str(self.nonce).encode()
        sha.update(nonce)
        return sha.hexdigest()

@dataclass
class PyChain:
    chain: List[Block]
    difficulty: int = 4

    def proof_of_work(self, block):
        calculated_hash = block.hash_block()
        num_of_zeros = "0" * self.difficulty
        while not calculated_hash.startswith(num_of_zeros):
            block.nonce += 1
            calculated_hash = block.hash_block()
        print("Winning Hash", calculated_hash)
        return block

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

    def is_valid(self):
        block_hash = self.chain[0].hash_block()
        for block in self.chain[1:]:
            if block_hash != block.prev_hash:
                print("Blockchain is invalid!")
                return False
            block_hash = block.hash_block()
        print("Blockchain is Valid")
        return True

################################################################################

# Streamlit Code

@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block(record=Record(sender="Genesis", receiver="", amount=0.0), creator_id=0)])

st.markdown("# PyChain")
st.markdown("## Store a Transaction Record in the PyChain")

pychain = setup()

################################################################################

# Step 3: Add Relevant User Inputs to the Streamlit Interface

# Delete the `input_data` variable from the Streamlit interface.
# input_data = st.text_input("Block Data")

# Add input areas for `sender`, `receiver`, and `amount`.
sender = st.text_input("Enter the sender")
receiver = st.text_input("Enter the receiver")
amount = st.number_input("Enter the amount", min_value=0.0)

if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    # Create a new Block with a Record
    new_block = Block(
        record=Record(sender=sender, receiver=receiver, amount=amount),
        creator_id=42,
        prev_hash=prev_block_hash
    )

    pychain.add_block(new_block)
    st.balloons()

################################################################################

# Streamlit Code (continues)

st.markdown("## The PyChain Ledger")
pychain_df = pd.DataFrame(pychain.chain).astype(str)
st.write(pychain_df)

difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 2)
pychain.difficulty = difficulty

st.sidebar.write("# Block Inspector")
selected_block = st.sidebar.selectbox(
    "Which block would you like to see?", pychain.chain
)

st.sidebar.write(selected_block)

if st.button("Validate Chain"):
    st.write(pychain.is_valid())

################################################################################