-- 1 An introduction to Agda for Haskell programmers
data Nat : Set where
    zero : Nat
    suc  : Nat → Nat

_+_ : Nat → Nat → Nat
zero + y = y
(suc x) + y = suc (x + y)

-- Exercise 1.1
halve : Nat → Nat
halve zero = zero
halve (suc zero) = zero
halve (suc (suc x)) = suc (halve x)

-- Exercise 1.2
_*_ : Nat → Nat → Nat
zero * x = zero
(suc x) * y = y + (x * y)

-- Exercise 1.3
data Bool : Set where
    true : Bool
    false : Bool
not : Bool → Bool
not true = false
not false = true
_&&_ : Bool → Bool → Bool
false && x = false
x && false = false
true && true = true
_||_ : Bool → Bool → Bool
true || x = true
x || true = true
false || false = false

id : {A : Set} → A → A
id x = x

if_then_else_ : {A : Set} → Bool → A → A → A
if true then x else y = x
if false then x else y = y

data List (A : Set) : Set where
    [] : List A
    _::_ : A → List A → List A

data _×_ (A B : Set) : Set where
    _,_ : A → B → A × B
infixr 4 _,_
infixr 5 _::_

fst : {A B : Set} → A × B → A
fst (x , y) = x
snd : {A B : Set} → A × B → B
snd (x , y) = y

-- Exercise 1.4
length : {A : Set} → List A → Nat
length [] = zero
length (h :: tl) = suc (length tl)

_++_ : {A : Set} → List A → List A → List A
[] ++ ys = ys
(x :: xs) ++ ys = x :: (xs ++ ys)

map : {A B : Set} → (A → B) → List A → List B
map f [] = []
map f (x :: xs) = (f x) :: (map f xs)

-- Exercise 1.5
data Maybe (A : Set) : Set where
    nothing : Maybe A
    just : A → Maybe A

lookup : {A : Set} → List A → Nat → Maybe A
lookup [] n = nothing
lookup (x :: xs) zero = just x
lookup (x :: xs) (suc n) = lookup xs n

-- 2 Dependent types