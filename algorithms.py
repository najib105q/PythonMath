import sys
import time
import random

# Maximale Rekursionstiefe erhöhen, um die Sortierung großer Eingaben zu unterstützen
sys.setrecursionlimit(2000)

# Implementierung von BubbleSort
def bubble_sort(arr):
    n = len(arr)  # Länge des Arrays bestimmen
    for i in range(n):  # Äußere Schleife für jeden Durchlauf
        for j in range(0, n - i - 1):  # Innere Schleife für den unsortierten Teil des Arrays
            if arr[j] > arr[j + 1]:  # Falls das aktuelle Element größer ist als das nächste
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Elemente tauschen
    return arr

# Verbesserte Implementierung von CubeSort mit begrenzter Rekursionstiefe
def cube_sort(arr):
    if len(arr) < 3:  # Basisfall: Falls das Array weniger als drei Elemente hat
        return bubble_sort(arr)  # Rückgriff auf BubbleSort für kleine Arrays
    
    # Bestimmen der Indexe zur Aufteilung des Arrays in drei Teile
    third = len(arr) // 3
    two_thirds = 2 * third
    
    # Rekursives Sortieren der drei Teile
    first_part = cube_sort(arr[:third])          # Sortiere das erste Drittel rekursiv
    second_part = cube_sort(arr[third:two_thirds])  # Sortiere das zweite Drittel rekursiv
    third_part = cube_sort(arr[two_thirds:])     # Sortiere das dritte Drittel rekursiv
    
    # Zusammenführen der drei sortierten Teile
    return merge(merge(first_part, second_part), third_part)

# Hilfsfunktion zum Zusammenführen von zwei sortierten Arrays
def merge(left, right):
    result = []  # Ergebnis-Array für die zusammengefügten Elemente
    i = j = 0    # Startindizes für linkes und rechtes Array
    
    # Durchlaufen der beiden Arrays, bis alle Elemente hinzugefügt wurden
    while i < len(left) and j < len(right):  # Schleife bis ein Array erschöpft ist
        if left[i] < right[j]:  # Falls Element des linken Arrays kleiner ist
            result.append(left[i])  # Füge Element des linken Arrays dem Ergebnis hinzu
            i += 1  # Index des linken Arrays erhöhen
        else:  # Falls Element des rechten Arrays kleiner oder gleich ist
            result.append(right[j])  # Füge Element des rechten Arrays dem Ergebnis hinzu
            j += 1  # Index des rechten Arrays erhöhen
    
    # Verbleibende Elemente aus beiden Arrays hinzufügen
    result.extend(left[i:])  # Alle restlichen Elemente aus dem linken Array
    result.extend(right[j:])  # Alle restlichen Elemente aus dem rechten Array
    return result  # Zusammengeführtes Ergebnis zurückgeben

# Implementierung von ExpoSort (eine rekursive Version, ähnlich QuickSort)
def expo_sort(arr):
    if len(arr) < 2:  # Basisfall: Falls das Array weniger als zwei Elemente hat, ist es sortiert
        return arr
    
    pivot = arr[0]  # Pivot-Element ist das erste Element
    less = [x for x in arr[1:] if x < pivot]  # Alle Elemente kleiner als Pivot
    greater = [x for x in arr[1:] if x >= pivot]  # Alle Elemente größer oder gleich dem Pivot
    
    # Rekursives Sortieren der kleineren und größeren Teile, gefolgt vom Pivot
    return expo_sort(less) + [pivot] + expo_sort(greater)

# Funktion zur Zeitmessung eines Sortieralgorithmus
def measure_time(sort_function, data):
    start = time.perf_counter()  # Startzeit messen
    sort_function(data.copy())  # Kopie des Arrays übergeben, um Original zu erhalten
    end = time.perf_counter()    # Endzeit messen
    return end - start  # Differenz als Laufzeit des Algorithmus zurückgeben

# Test und Zeitvergleich für Listen unterschiedlicher Längen
lengths = [10, 20, 50, 5000]  # Verschiedene Eingabelängen für die Messung
results = {"BubbleSort": [], "ExpoSort": [], "CubeSort": []}  # Ergebnis-Container

# Zeitmessung für verschiedene Array-Größen
for length in lengths:
    data = [random.randint(0, 100000) for _ in range(length)]  # Generiere ein zufälliges Array
    results["BubbleSort"].append(measure_time(bubble_sort, data))  # Zeit für BubbleSort messen
    results["ExpoSort"].append(measure_time(expo_sort, data))      # Zeit für ExpoSort messen
    results["CubeSort"].append(measure_time(cube_sort, data))      # Zeit für CubeSort messen

# Ausgabe der Laufzeiten für die verschiedenen Sortieralgorithmen und Eingabelängen
for sort_type, times in results.items():
    print(f"{sort_type} Zeiten (Sekunden):")
    for length, time_taken in zip(lengths, times):
        print(f"  Länge {length}: {time_taken:.6f} Sekunden")
