use std::sync::Arc;
use std::fmt::Debug;

/// Una Conc‑tree list inmutable y persistente, diseñada para operaciones funcionales.
#[derive(Clone, Debug)]
pub enum ConcTreeList<T> {
    /// Nodo vacío.
    Empty,
    /// Nodo que contiene un único elemento.
    Single(T),
    /// Nodo interno que concatena dos subárboles y guarda el tamaño total.
    Append {
        size: usize,
        left: Arc<ConcTreeList<T>>,
        right: Arc<ConcTreeList<T>>,
    },
}

// Funciones básicas que no requieren T: Clone.
impl<T> ConcTreeList<T> {
    /// Crea una nueva ConcTreeList vacía.
    pub fn new() -> Self {
        ConcTreeList::Empty
    }

    /// Retorna la cantidad de elementos en la ConcTreeList.
    pub fn len(&self) -> usize {
        match self {
            ConcTreeList::Empty => 0,
            ConcTreeList::Single(_) => 1,
            ConcTreeList::Append { size, .. } => *size,
        }
    }

    /// Indica si la ConcTreeList está vacía.
    pub fn is_empty(&self) -> bool {
        self.len() == 0
    }

    /// Crea una ConcTreeList con un único elemento.
    pub fn single(elem: T) -> Self {
        ConcTreeList::Single(elem)
    }

    /// Concatena dos ConcTreeList y retorna la lista resultante.
    /// Si alguno está vacío, retorna el otro.
    pub fn concat(self, other: Self) -> Self {
        if self.is_empty() {
            other
        } else if other.is_empty() {
            self
        } else {
            let size = self.len() + other.len();
            ConcTreeList::Append {
                size,
                left: Arc::new(self),
                right: Arc::new(other),
            }
        }
    }

    /// Retorna una referencia al elemento en la posición `index`, o `None` si no existe.
    pub fn get(&self, index: usize) -> Option<&T> {
        match self {
            ConcTreeList::Empty => None,
            ConcTreeList::Single(x) => {
                if index == 0 {
                    Some(x)
                } else {
                    None
                }
            }
            ConcTreeList::Append { left, right, .. } => {
                let left_len = left.len();
                if index < left_len {
                    left.get(index)
                } else {
                    right.get(index - left_len)
                }
            }
        }
    }

    /// Retorna un iterador sobre los elementos de la ConcTreeList.
    pub fn iter(&self) -> ConcTreeListIter<T> {
        ConcTreeListIter::new(self)
    }
}

/// Iterador que recorre el árbol en orden (depth-first, izquierda a derecha).
pub struct ConcTreeListIter<'a, T> {
    stack: Vec<&'a ConcTreeList<T>>,
}

impl<'a, T> ConcTreeListIter<'a, T> {
    fn new(tree: &'a ConcTreeList<T>) -> Self {
        let mut stack = Vec::new();
        stack.push(tree);
        Self { stack }
    }
}

impl<'a, T> Iterator for ConcTreeListIter<'a, T> {
    type Item = &'a T;

    fn next(&mut self) -> Option<Self::Item> {
        while let Some(node) = self.stack.pop() {
            match node {
                ConcTreeList::Empty => continue,
                ConcTreeList::Single(x) => return Some(x),
                ConcTreeList::Append { left, right, .. } => {
                    // Se empuja primero el subárbol derecho para procesar el izquierdo primero.
                    self.stack.push(right);
                    self.stack.push(left);
                }
            }
        }
        None
    }
}

// Funciones que requieren T: Clone (como reconstrucción y modificación de la estructura).
impl<T: Clone> ConcTreeList<T> {
    /// "Rebalancea" el árbol, reconstruyéndolo de forma balanceada.
    pub fn rebalance(&self) -> Self {
        let vec: Vec<T> = self.iter().cloned().collect();
        Self::from_vec(vec)
    }

    /// Construye una ConcTreeList a partir de un vector, generando un árbol balanceado.
    pub fn from_vec(vec: Vec<T>) -> Self {
        Self::from_slice(&vec)
    }

    /// Construye una ConcTreeList a partir de un slice, generando un árbol balanceado.
    pub fn from_slice(slice: &[T]) -> Self {
        let n = slice.len();
        if n == 0 {
            Self::new()
        } else if n == 1 {
            Self::single(slice[0].clone())
        } else {
            let mid = n / 2;
            let left = Self::from_slice(&slice[..mid]);
            let right = Self::from_slice(&slice[mid..]);
            left.concat(right)
        }
    }

    /// Elimina el elemento en la posición `index` y retorna una nueva ConcTreeList.
    /// La operación se realiza recursivamente, reconstruyendo únicamente las ramas afectadas.
    pub fn delete_at(&self, index: usize) -> Self {
        assert!(index < self.len(), "Index out of bounds");
        match self {
            ConcTreeList::Empty => Self::Empty,
            ConcTreeList::Single(_) => {
                if index == 0 {
                    Self::Empty
                } else {
                    unreachable!("Index out of bounds")
                }
            }
            ConcTreeList::Append { left, right, .. } => {
                let left_len = left.len();
                if index < left_len {
                    let new_left = left.delete_at(index);
                    new_left.concat((**right).clone())
                } else {
                    let new_right = right.delete_at(index - left_len);
                    // Clonamos el valor interno de left usando doble dereferenciación.
                    let left_val: ConcTreeList<T> = (**left).clone();
                    left_val.concat(new_right)
                }
            }
        }
    }

    /// Inserta un elemento en la posición `index` y retorna la nueva ConcTreeList.
    /// Si `index == 0`, se inserta al inicio; si `index == self.len()`, se inserta al final.
    pub fn insert_at(&self, index: usize, elem: T) -> Self {
        assert!(index <= self.len(), "Index out of bounds");
        match self {
            ConcTreeList::Empty => {
                if index == 0 {
                    Self::single(elem)
                } else {
                    unreachable!("Index out of bounds")
                }
            }
            ConcTreeList::Single(x) => {
                if index == 0 {
                    Self::single(elem).concat(Self::single(x.clone()))
                } else if index == 1 {
                    Self::single(x.clone()).concat(Self::single(elem))
                } else {
                    unreachable!("Index out of bounds")
                }
            }
            ConcTreeList::Append { left, right, .. } => {
                let left_len = left.len();
                if index <= left_len {
                    let new_left = left.insert_at(index, elem);
                    new_left.concat((**right).clone())
                } else {
                    let new_right = right.insert_at(index - left_len, elem);
                    // Clonamos el valor interno de left usando doble dereferenciación.
                    let left_val: ConcTreeList<T> = (**left).clone();
                    left_val.concat(new_right)
                }
            }
        }
    }
}



#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_empty() {
        let tree: ConcTreeList<i32> = ConcTreeList::new();
        assert_eq!(tree.len(), 0);
        assert!(tree.is_empty());
        assert_eq!(tree.get(0), None);
    }

    #[test]
    fn test_single() {
        let tree = ConcTreeList::single(42);
        assert_eq!(tree.len(), 1);
        assert!(!tree.is_empty());
        assert_eq!(tree.get(0), Some(&42));
        assert_eq!(tree.get(1), None);
    }

    #[test]
    fn test_concat() {
        let t1 = ConcTreeList::single(1);
        let t2 = ConcTreeList::single(2);
        let t3 = t1.clone().concat(t2.clone());
        assert_eq!(t3.len(), 2);
        assert_eq!(t3.get(0), Some(&1));
        assert_eq!(t3.get(1), Some(&2));

        let t4 = t3.concat(ConcTreeList::single(3));
        assert_eq!(t4.len(), 3);
        assert_eq!(t4.get(0), Some(&1));
        assert_eq!(t4.get(1), Some(&2));
        assert_eq!(t4.get(2), Some(&3));
    }

    #[test]
    fn test_iter() {
        let t1 = ConcTreeList::single(1);
        let t2 = ConcTreeList::single(2);
        let t3 = ConcTreeList::single(3);
        let tree = t1.concat(t2).concat(t3);
        let v: Vec<i32> = tree.iter().cloned().collect();
        assert_eq!(v, vec![1, 2, 3]);
    }

    #[test]
    fn test_rebalance() {
        // Build a degenerate tree by concatenating many Singles sequentially.
        let mut tree = ConcTreeList::new();
        for i in 0..100 {
            tree = tree.concat(ConcTreeList::single(i));
        }
        assert_eq!(tree.len(), 100);
        // Rebalance and verify the sequence.
        let balanced = tree.rebalance();
        let v: Vec<i32> = balanced.iter().cloned().collect();
        assert_eq!(v, (0..100).collect::<Vec<i32>>());
    }

    #[test]
    fn test_delete_at() {
        // Create a balanced tree with elements [0, 1, 2, 3, 4]
        let tree = ConcTreeList::from_vec(vec![0, 1, 2, 3, 4]);
        
        // Delete the element at index 2 (value 2) -> expected: [0, 1, 3, 4]
        let tree_after = tree.delete_at(2);
        assert_eq!(tree_after.len(), 4);
        let v: Vec<i32> = tree_after.iter().cloned().collect();
        assert_eq!(v, vec![0, 1, 3, 4]);

        // Delete the element at index 0 (value 0) -> expected: [1, 2, 3, 4]
        let tree_after = tree.delete_at(0);
        assert_eq!(tree_after.len(), 4);
        let v: Vec<i32> = tree_after.iter().cloned().collect();
        assert_eq!(v, vec![1, 2, 3, 4]);

        // Delete the element at the last index (value 4) -> expected: [0, 1, 2, 3]
        let tree_after = tree.delete_at(tree.len() - 1);
        assert_eq!(tree_after.len(), 4);
        let v: Vec<i32> = tree_after.iter().cloned().collect();
        assert_eq!(v, vec![0, 1, 2, 3]);
    }

    #[test]
    fn test_insert_at() {
        // Create a balanced tree with elements [1, 3, 4]
        let tree = ConcTreeList::from_vec(vec![1, 3, 4]);
        
        // Insert 2 at index 1 -> expected: [1, 2, 3, 4]
        let tree_after = tree.insert_at(1, 2);
        assert_eq!(tree_after.len(), 4);
        let v: Vec<i32> = tree_after.iter().cloned().collect();
        assert_eq!(v, vec![1, 2, 3, 4]);

        // Insert 0 at the beginning (index 0) -> expected: [0, 1, 3, 4]
        let tree_after = tree.insert_at(0, 0);
        let v: Vec<i32> = tree_after.iter().cloned().collect();
        assert_eq!(v, vec![0, 1, 3, 4]);

        // Insert 5 at the end (index = tree.len()) -> expected: [1, 3, 4, 5]
        let tree_after = tree.insert_at(tree.len(), 5);
        let v: Vec<i32> = tree_after.iter().cloned().collect();
        assert_eq!(v, vec![1, 3, 4, 5]);
    }

    #[test]
    fn test_insert_at_single() {
        let tree = ConcTreeList::single(10);
        // Insert before the single element.
        let tree_before = tree.insert_at(0, 5); // expected: [5, 10]
        let v: Vec<i32> = tree_before.iter().cloned().collect();
        assert_eq!(v, vec![5, 10]);

        // Insert after the single element.
        let tree_after = tree.insert_at(1, 15); // expected: [10, 15]
        let v: Vec<i32> = tree_after.iter().cloned().collect();
        assert_eq!(v, vec![10, 15]);
    }
}
