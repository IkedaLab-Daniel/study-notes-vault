//* keyof

type DatePropertyNames = keyof Date

type DateStringPropertyNames = DatePropertyNames & string
type DateSymbolPropertyNames = DatePropertyNames & symbol

//* typeof

async function main() {
    const apiResponse = await Promise.all([
        fetch("https://example.com"),
        Promise.resolve("Titanium White"),
    ])
    type ApiResponseType = typeof apiResponse
}

//?^ note: type alias within a function scope!
const MyRule = CSSRule
CSSRule.STYLE_RULE
const foo = new MyRule()

type MyRule = typeof MyRule


//* Indexed Access Types


// interface Car {
//     make: string
//     model: string
//     year: number
//     color: {
//         red: string
//         green: string
//         blue: string
//     }
// }

// let carColor: Car["color"] //✔️ Reaching for something that exists
// let carSomething: Car["not-something-on-car"] //! Reaching for something invalid
// let carColorRedComponent: Car["color"]["red"] //✔️ Reaching for something nested
// let carProperty: Car["color" | "year"] // ✔️ Passing a union type through the index

//* Use case: the type registry pattern
/*
// See: 
import("./09-type-registry/")

/**/
export default {}
