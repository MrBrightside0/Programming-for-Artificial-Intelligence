import processing
import normalization

def main():
    print("=== AMAZON DATA MANAGEMENT & NORMALIZATION SYSTEM ===\n")

    path = "data/amazon.csv"
    df = processing.load_data(path)
    df_clean = processing.clean_data(df)

    tables = normalization.normalize_data(df_clean)
    processing.save_results(tables, "results")

    print("\n✅ Process completed successfully. Normalized files saved in /results")

if __name__ == "__main__":
    main()
