import it from './it.json';
import es from './es.json';
import en from './en.json';

export type Locale = 'it' | 'es' | 'en';
export const defaultLocale: Locale = 'it';

type Dict = Record<string, string>;
const dictionaries: Record<Locale, Dict> = { it, es, en };

/**
 * Restituisce la stringa per la chiave nella lingua richiesta.
 * Se manca in es/en ricade sull'italiano; se manca anche lì, restituisce la chiave.
 */
export function t(locale: Locale, key: string): string {
  return dictionaries[locale]?.[key] ?? dictionaries[defaultLocale][key] ?? key;
}
