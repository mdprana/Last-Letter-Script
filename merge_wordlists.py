import os
import re

def merge_files(output_file, input_files):
    unique_words = set()
    total_words_processed = 0
    files_processed = 0

    print("=" * 70)
    print("ULTIMATE WORD LIST MERGER")
    print("=" * 70)
    print()

    for file_path in input_files:
        if not os.path.exists(file_path):
            print(f"[WARNING] {file_path} not found. Skipping.")
            continue
            
        print(f"[PROCESSING] {file_path}")
        files_processed += 1
        words_in_file = 0
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                for line in f:
                    # Strip whitespace and convert to lowercase
                    clean_line = line.strip().lower()
                    
                    # Remove any non-alphabetic characters
                    clean_line = re.sub(r'[^a-z]', '', clean_line)
                    
                    # Only add if it's a valid word (2+ letters, all alphabetic)
                    if len(clean_line) >= 2 and clean_line.isalpha():
                        unique_words.add(clean_line)
                        words_in_file += 1
                        total_words_processed += 1
                        
            print(f"   [OK] Words found: {words_in_file:,}")
            print(f"   [OK] Unique total: {len(unique_words):,}")
            print()
            
        except Exception as e:
            print(f"   [ERROR] Error reading file: {e}")
            print()

    print("=" * 70)
    print("PROCESSING COMPLETE")
    print("=" * 70)
    print(f"Files processed: {files_processed}")
    print(f"Total words processed: {total_words_processed:,}")
    print(f"Unique words found: {len(unique_words):,}")
    print(f"Duplicates removed: {total_words_processed - len(unique_words):,}")
    print()

    # Sort words alphabetically
    print("Sorting words alphabetically...")
    sorted_words = sorted(unique_words)
    
    # Write to output file
    print(f"Writing to {output_file}...")
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for word in sorted_words:
                f.write(word + '\n')
        
        # Get file size
        file_size = os.path.getsize(output_file)
        file_size_mb = file_size / (1024 * 1024)
        
        print()
        print("=" * 70)
        print("SUCCESS!")
        print("=" * 70)
        print(f"Output file: {output_file}")
        print(f"Total unique words: {len(sorted_words):,}")
        print(f"File size: {file_size_mb:.2f} MB ({file_size:,} bytes)")
        print()
        
        # Show statistics
        print("WORD LENGTH DISTRIBUTION:")
        print("-" * 70)
        length_dist = {}
        for word in sorted_words:
            length = len(word)
            length_dist[length] = length_dist.get(length, 0) + 1
        
        for length in sorted(length_dist.keys())[:20]:  # Show first 20
            count = length_dist[length]
            percentage = (count / len(sorted_words)) * 100
            bar = '#' * min(50, int(percentage * 2))
            print(f"{length:2d} letters: {count:7,} words ({percentage:5.2f}%) {bar}")
        
        print()
        print("FIRST LETTER DISTRIBUTION:")
        print("-" * 70)
        first_letter_dist = {}
        for word in sorted_words:
            letter = word[0]
            first_letter_dist[letter] = first_letter_dist.get(letter, 0) + 1
        
        for letter in sorted(first_letter_dist.keys()):
            count = first_letter_dist[letter]
            percentage = (count / len(sorted_words)) * 100
            bar = '#' * min(50, int(percentage))
            print(f"{letter.upper()}: {count:7,} words ({percentage:5.2f}%) {bar}")
        
        print()
        print("SAMPLE WORDS:")
        print("-" * 70)
        print("First 20 words:")
        for i, word in enumerate(sorted_words[:20], 1):
            print(f"  {i:2d}. {word}")
        
        print()
        print("Last 20 words:")
        for i, word in enumerate(sorted_words[-20:], len(sorted_words)-19):
            print(f"  {i:7,}. {word}")
        
        print()
        print("=" * 70)
        print("DONE!")
        print("=" * 70)
        
    except Exception as e:
        print(f"[ERROR] Error writing to {output_file}: {e}")

if __name__ == "__main__":
    # List of files to merge
    files_to_merge = [
        "./wordlists/british_english.txt",
        "./wordlists/dwylans_english.txt",
        "./wordlists/enable1_scrabble.txt",
        "./wordlists/english_ultimate.txt",
        "./wordlists/google_10k.txt",
        "./wordlists/google-10000-english-no-swears.txt",
        "./wordlists/merged_english.txt",
        "./wordlists/top_english_adjs_lower_100000.txt",
        "./wordlists/top_english_adps_lower_500.txt",
        "./wordlists/top_english_advs_lower_10000.txt",
        "./wordlists/top_english_conjs_lower_500.txt",
        "./wordlists/top_english_dets_lower_500.txt",
        "./wordlists/top_english_nouns_lower_500000.txt",
        "./wordlists/top_english_nums_lower_500.txt",
        "./wordlists/top_english_prons_lower_10000.txt",
        "./wordlists/top_english_prts_lower_500.txt",
        "./wordlists/top_english_verbs_lower_100000.txt",
        "./wordlists/top_english_words_lower_1000000.txt",
        "./wordlists/words_alpha.txt"
    ]
    
    output_filename = "ultimate_merged_english.txt"
    
    merge_files(output_filename, files_to_merge)
