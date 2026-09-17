"use client"

import * as React from "react"
import { Search, X } from "lucide-react"
import {
  InputGroup,
  InputGroupAddon,
  InputGroupButton,
  InputGroupInput,
} from "@/components/ui/input-group"
import { Button } from "@/components/ui/button"

interface SearchBarProps {
  onSearch: (value: string) => void
  initialValue?: string
}

export function SearchBar({ onSearch, initialValue = "" }: SearchBarProps) {
  const [value, setValue] = React.useState(initialValue)

  const onSearchRef = React.useRef(onSearch)
  React.useEffect(() => {
    onSearchRef.current = onSearch
  }, [onSearch])

  // Debounce live search so results update as the user types.
  React.useEffect(() => {
    const trimmed = value.trim()
    const timeout = setTimeout(() => {
      onSearchRef.current(trimmed)
    }, 400)
    return () => clearTimeout(timeout)
  }, [value])

  function handleSubmit(event: React.FormEvent) {
    event.preventDefault()
    onSearch(value.trim())
  }

  function handleClear() {
    setValue("")
    onSearch("")
  }

  return (
    <form onSubmit={handleSubmit} className="flex w-full items-center gap-2">
      <InputGroup className="h-12 rounded-xl bg-card shadow-sm">
        <InputGroupAddon>
          <Search className="text-muted-foreground" />
        </InputGroupAddon>
        <InputGroupInput
          value={value}
          onChange={(e) => setValue(e.target.value)}
          placeholder="Search by title, author, or keyword..."
          aria-label="Search books"
          className="text-base"
        />
        {value.length > 0 && (
          <InputGroupAddon align="inline-end">
            <InputGroupButton
              type="button"
              size="icon-xs"
              aria-label="Clear search"
              onClick={handleClear}
            >
              <X />
            </InputGroupButton>
          </InputGroupAddon>
        )}
      </InputGroup>
      <Button type="submit" size="lg" className="h-12 shrink-0 px-6">
        Search
      </Button>
    </form>
  )
}
