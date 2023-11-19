-- Curry Howard Correspondence
open import Agda.Builtin.Nat
open import Agda.Builtin.Bool

data ⊤ : Set where
    tt : ⊤

data ⊥ : Set where
    -- no constructors

absurd : {A : Set} → ⊥ → A
absurd ()

data Either (A B : Set) : Set where
    left : A → Either A B
    right : B → Either A B

data _×_ (A B : Set) : Set where
    _,_ : A → B → A × B

proof3 : {P Q R : Set} → (Either P Q → R) → (P → R) × (Q → R)
proof3 f = (λ x → f (left x)) , (λ y → f (right y))

-- excluded-middle : {P : Set} → (Either P (P → ⊥) → ⊥) → ⊥
-- excluded-middle ei = {!!}

data IsEven : Nat → Set where
    even-zero : IsEven zero
    even-suc2 : {n : Nat} → IsEven n → IsEven (suc (suc n))

6-is-even : IsEven 6
6-is-even = even-suc2 (even-suc2 (even-suc2 even-zero))

-- works because we do pattern matching on variable in
-- 7-is-not-even x = {!!}
7-is-not-even : IsEven 7 → ⊥
7-is-not-even (even-suc2 (even-suc2 (even-suc2 ())))

data IsTrue : Bool → Set where
    is-true : IsTrue true

_=Nat_ : Nat → Nat → Bool
zero =Nat zero = true
(suc x) =Nat (suc y) = x =Nat y
_ =Nat _ = false

data List (A : Set) : Set where
    [] : List A
    _::_ : A → List A → List A
infixr 5 _::_
length : {A : Set} → List A → Nat
length [] = zero
length (h :: tl) = suc (length tl)
length-is-3 : IsTrue (length (1 :: 2 :: 3 :: []) =Nat 3)
length-is-3 = is-true

double : Nat → Nat
double zero = zero
double (suc n) = suc (suc (double n))
double-is-even : (n : Nat) → IsEven (double n)
double-is-even zero = even-zero
double-is-even (suc m) = even-suc2 (double-is-even m)

n-equals-n : (n : Nat) → IsTrue (n =Nat n)
n-equals-n zero = is-true
n-equals-n (suc m) = n-equals-n m

data Σ (A : Set) (B : A → Set) : Set where
    _,_ : (x : A) → B x → Σ A B

zero-or-suc : (n : Nat) → Either (IsTrue (n =Nat 0)) (Σ Nat (λ m → IsTrue (n =Nat (suc m))))

zero-or-suc zero = left is-true
zero-or-suc (suc x) = right (x , n-equals-n x)


data _≡_ {A : Set} : A → A → Set where
    refl : {x : A} → x ≡ x
infix 4 _≡_

id : {A : Set} → A → A
id x = x

one-plus-one : 1 + 1 ≡ 2
one-plus-one = refl

two-not-three : 2 ≡ 3 → ⊥
two-not-three ()

-- symmetry of equality
sym : {A : Set} {x y : A} → x ≡ y → y ≡ x
sym refl = refl
-- sym refl = refl
-- transitivity of equality
trans : {A : Set} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
trans refl refl = refl
-- trans refl refl = refl
-- congruence of equality
cong : {A B : Set} {x y : A} → (f : A → B) → x ≡ y → f x ≡ f y
cong f refl = refl