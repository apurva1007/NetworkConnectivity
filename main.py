from quick_find import QuickFind
from quick_union import  QuickUnion
from weighted_quick_union import WeightedQuickUnion
from weighted_quick_union_path_compression import WeightedQuickUnionPathCompression
from find_largest_node_in_the_component import FindLargestNodeInTheComponent

n = 10

print("Select Method:")
print("1. Quick Find")
print("2. Quick Union")
print("3. Weighted Quick Union")
print("4. Weighted Quick Union with Path Compression")
print("5. Find largest node")
choice = int(input("Enter your choice: "))

if choice == 1:
    quick_find = QuickFind(n)
    quick_find.union(4, 3)
    quick_find.union(3, 8)
    quick_find.union(6, 5)
    quick_find.union(9, 4)
    quick_find.union(2, 1)
    quick_find.union(5, 0)
    quick_find.union(7, 2)
    quick_find.union(6, 1)
    quick_find.connected(0, 9)

elif choice == 2:
    quick_union = QuickUnion(n)
    quick_union.union(4, 3)
    quick_union.union(3, 8)
    quick_union.union(6, 5)
    quick_union.union(9, 4)
    quick_union.union(2, 1)
    quick_union.union(5, 0)
    quick_union.union(7, 2)
    quick_union.union(6, 1)
    quick_union.connected(0, 9)

elif choice == 3:
    weighted_quick_union = WeightedQuickUnion(n)
    weighted_quick_union.union(4, 3)
    weighted_quick_union.union(3, 8)
    weighted_quick_union.union(6, 5)
    weighted_quick_union.union(9, 4)
    weighted_quick_union.union(2, 1)
    weighted_quick_union.union(5, 0)
    weighted_quick_union.union(7, 2)
    weighted_quick_union.union(6, 1)
    weighted_quick_union.union(7, 3)
    weighted_quick_union.connected(0, 9)

elif choice == 4:
    weighted_quick_union_path_compression = WeightedQuickUnionPathCompression(n)
    weighted_quick_union_path_compression.union(4, 3)
    weighted_quick_union_path_compression.union(3, 8)
    weighted_quick_union_path_compression.union(6, 5)
    weighted_quick_union_path_compression.union(9, 4)
    weighted_quick_union_path_compression.union(2, 1)
    weighted_quick_union_path_compression.union(5, 0)
    weighted_quick_union_path_compression.union(7, 2)
    weighted_quick_union_path_compression.union(6, 1)
    weighted_quick_union_path_compression.union(7, 3)
    weighted_quick_union_path_compression.connected(0, 9)

elif choice == 5:
    find_largest_node_in_the_component = FindLargestNodeInTheComponent(n)

    find_largest_node_in_the_component.union(4, 3)
    find_largest_node_in_the_component.union(3, 8)
    find_largest_node_in_the_component.union(6, 5)
    find_largest_node_in_the_component.union(9, 4)
    find_largest_node_in_the_component.union(2, 1)
    find_largest_node_in_the_component.union(5, 0)
    find_largest_node_in_the_component.union(7, 2)
    find_largest_node_in_the_component.union(6, 1)
    find_largest_node_in_the_component.union(7, 3)

    i = int(input('Enter i (0-9): '))
    largest = find_largest_node_in_the_component.find(i)
    print("Largest element in the component containing", i, "is", largest)


