import { type NextRequest, NextResponse } from "next/server"
import type { BookDetail } from "@/lib/types"

interface WorkResponse {
  description?: string | { value?: string }
  subjects?: string[]
  subject_people?: string[]
  subject_places?: string[]
  first_publish_date?: string
}

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url)
  const key = searchParams.get("key")?.trim()

  if (!key) {
    return NextResponse.json({ error: "Missing work key" }, { status: 400 })
  }

  const url = `https://openlibrary.org${key}.json`

  try {
    const res = await fetch(url, {
      headers: { "User-Agent": "LibraryBookFinder/1.0" },
      next: { revalidate: 86400 },
    })

    if (!res.ok) {
      return NextResponse.json({ error: "Failed to fetch details" }, { status: 502 })
    }

    const data = (await res.json()) as WorkResponse
    const description =
      typeof data.description === "string"
        ? data.description
        : (data.description?.value ?? null)

    const payload: BookDetail = {
      description,
      subjects: (data.subjects ?? []).slice(0, 12),
      subjectPeople: (data.subject_people ?? []).slice(0, 8),
      subjectPlaces: (data.subject_places ?? []).slice(0, 8),
      firstPublishDate: data.first_publish_date ?? null,
    }

    return NextResponse.json(payload)
  } catch {
    return NextResponse.json({ error: "Failed to reach the library" }, { status: 500 })
  }
}
