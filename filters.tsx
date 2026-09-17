"use client"

import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"

export const SUBJECTS = [
  { value: "all", label: "All subjects" },
  { value: "fiction", label: "Fiction" },
  { value: "fantasy", label: "Fantasy" },
  { value: "science_fiction", label: "Science Fiction" },
  { value: "mystery", label: "Mystery" },
  { value: "romance", label: "Romance" },
  { value: "thriller", label: "Thriller" },
  { value: "horror", label: "Horror" },
  { value: "history", label: "History" },
  { value: "biography", label: "Biography" },
  { value: "science", label: "Science" },
  { value: "poetry", label: "Poetry" },
  { value: "juvenile", label: "Children's" },
]

export const SORTS = [
  { value: "relevance", label: "Relevance" },
  { value: "new", label: "Newest first" },
  { value: "old", label: "Oldest first" },
  { value: "rating", label: "Top rated" },
  { value: "editions", label: "Most editions" },
]

interface FiltersProps {
  subject: string
  sort: string
  onSubjectChange: (value: string) => void
  onSortChange: (value: string) => void
}

export function Filters({
  subject,
  sort,
  onSubjectChange,
  onSortChange,
}: FiltersProps) {
  return (
    <div className="flex flex-col gap-3 sm:flex-row sm:items-center">
      <div className="flex flex-1 flex-col gap-1.5">
        <label className="text-xs font-medium text-muted-foreground">
          Subject
        </label>
        <Select value={subject} onValueChange={(v) => onSubjectChange(v as string)}>
          <SelectTrigger className="h-10 w-full">
            <SelectValue placeholder="All subjects" />
          </SelectTrigger>
          <SelectContent>
            <SelectGroup>
              {SUBJECTS.map((s) => (
                <SelectItem key={s.value} value={s.value}>
                  {s.label}
                </SelectItem>
              ))}
            </SelectGroup>
          </SelectContent>
        </Select>
      </div>
      <div className="flex flex-1 flex-col gap-1.5">
        <label className="text-xs font-medium text-muted-foreground">
          Sort by
        </label>
        <Select value={sort} onValueChange={(v) => onSortChange(v as string)}>
          <SelectTrigger className="h-10 w-full">
            <SelectValue placeholder="Relevance" />
          </SelectTrigger>
          <SelectContent>
            <SelectGroup>
              {SORTS.map((s) => (
                <SelectItem key={s.value} value={s.value}>
                  {s.label}
                </SelectItem>
              ))}
            </SelectGroup>
          </SelectContent>
        </Select>
      </div>
    </div>
  )
}
