export interface Book {
  key: string
  title: string
  authors: string[]
  firstPublishYear: number | null
  coverId: number | null
  editionCount: number
  subjects: string[]
  ratingsAverage: number | null
  ratingsCount: number | null
  languages: string[]
  pages: number | null
  ebookAccess: string | null
}

export interface SearchResponse {
  books: Book[]
  total: number
  page: number
  perPage: number
}

export interface BookDetail {
  description: string | null
  subjects: string[]
  subjectPeople: string[]
  subjectPlaces: string[]
  firstPublishDate: string | null
}

export function coverUrl(coverId: number | null, size: "S" | "M" | "L" = "M") {
  if (!coverId) return null
  return `https://covers.openlibrary.org/b/id/${coverId}-${size}.jpg`
}
