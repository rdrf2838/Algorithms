data Nat : Set where
    zero : Nat
    suc  : Nat → Nat

_+_ : Nat → Nat → Nat
zero + y = y
(suc x) + y = suc (x + y)

-- data Vec : Set → Nat → Set where
--     [] : {A : Set} → Vec A zero
--     _::_ : {A : Set} → {n : Nat} → A → Vec A n → Vec A (suc n)

data Vec (A : Set) : Nat → Set where
    [] : Vec A zero
    _::_ : {n : Nat} → A → Vec A n → Vec A (suc n)

infixr 5 _::_

_++Vec_ : {A : Set} {m n : Nat} → Vec A m → Vec A n → Vec A (m + n)
[] ++Vec ys = ys
(x :: xs) ++Vec ys = x :: (xs ++Vec ys)

head : {A : Set}{n : Nat} → Vec A (suc n) → A
head (x :: xs) = x

data Fin : Nat → Set where
    zero : {n : Nat} → Fin (suc n)
    suc : {n : Nat} → Fin n → Fin (suc n)

lookupVec : {A : Set} {n : Nat} → Vec A n → Fin n → A
lookupVec (x :: xs) zero = x
lookupVec (x :: xs) (suc i) = lookupVec xs i

-- Exercise 2.4. 
putVec : {A : Set}{n : Nat} → Fin n → A → Vec A n → Vec A n
putVec zero a (x :: xs) = a :: xs
putVec (suc i) a (x :: xs) = x :: (putVec i a xs)

data Σ (A : Set) (B : A → Set) : Set where
    _,_ : (x : A) → B x → Σ A B

fstΣ : {A : Set}{B : A → Set} → Σ A B → A
fstΣ (x , y) = x
sndΣ : {A : Set}{B : A → Set} → (z : Σ A B) → B (fstΣ z)
sndΣ (x , y) = y

-- Exercise 2.5
data _×_ (A B : Set) : Set where
    _,_ : A → B → A × B
infixr 4 _,_
fst : {A B : Set} → A × B → A
fst (a , b) = a
snd : {A B : Set} → A × B → B
snd (a , b) = b

_×'_ : (A B : Set) → Set
A ×' B = Σ A (λ _ → B)

modifyTimes : {A B : Set} → A × B → A ×' B
modifyTimes (a , b) = (a , b)

-- Exercise 2.6
data List (A : Set) : Set where
    [] : List A
    _::_ : A → List A → List A

List' : (A : Set) → Set
List' A = Σ Nat (Vec A)

[]' : {A : Set} → List' A
[]' = (zero , [])
_::'_ : {A : Set} → A → List' A → List' A
x ::' (x₁ , x₂) = (suc x₁) , (x :: x₂)

modifyList : {A : Set} → List A → List' A
modifyList [] = []'
modifyList (x :: xs) = x ::' (modifyList xs)