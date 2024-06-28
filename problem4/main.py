def count_item_and_sort(items):
    # Hitung frekuensi setiap item dalam list
    item_counts = {}
    for item in items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1

    # Urutkan item berdasarkan frekuensi dan nama
    sorted_items = sorted(item_counts.items(), key=lambda x: (x[1], x[0]))

    # Format hasil menjadi string sesuai dengan format yang diinginkan
    result = ' '.join([f"{item}->{count}" for item, count in sorted_items])

    return result

if __name__ == "__main__":
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
    # "golang->1 ruby->2 js->4"
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
    # "C->1 D->2 B->3 A->4"
    print(count_item_and_sort(["football", "basketball", "tenis"]))
    # "basketball->1 football->1 tenis->1"