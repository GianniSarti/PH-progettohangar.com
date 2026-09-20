import { useState } from 'react';

interface Props {
  label: string;
}

// Isola React di prova: verifica che @astrojs/react funzioni.
export default function Counter({ label }: Props) {
  const [count, setCount] = useState(0);
  return (
    <button
      type="button"
      className="rounded bg-slate-800 px-4 py-2 text-white hover:bg-slate-700"
      onClick={() => setCount(count + 1)}
    >
      {label} {count}
    </button>
  );
}
