from pathlib import Path
import pandas as pd

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
INPUT_FILE   = "C:\\Users\\crazy\\OneDrive\\LII\\docs.csv"        # Path to the 2‑column CSV to read
OUTPUT_FILE  = "C:\\Users\\crazy\\OneDrive\\LII\\doc_nodes.csv"   # Set to a filename, or leave None to auto‑name
DELIMITER    = ","               # Change if your CSV uses another delimiter
HAS_HEADER   = True             # True if the first row is a header 
# ----------------------------------------------------------------------

# Load the CSV
df = pd.read_csv(
    INPUT_FILE,
    delimiter=DELIMITER,
    header=0 if HAS_HEADER else None,
    dtype=str,            # keep everything as strings
)

# Stack the two columns and remove duplicates
cols = [df[col].squeeze() for col in df.columns]   # list of Series
stacked = pd.concat(cols, ignore_index=True)       # one long Series

stacked = stacked.drop_duplicates(keep="first").reset_index(drop=True)

# Determine the output filename 
if OUTPUT_FILE:
    out_path = Path(OUTPUT_FILE)
else:
    src = Path(INPUT_FILE)
    out_path = src.with_name(f"{src.stem}_stacked{src.suffix or '.csv'}")

# Save the single‑column CSV 
stacked.to_csv(out_path, index=False, header=False)
print(f"✅  Stacked column written to: {out_path.resolve()}")