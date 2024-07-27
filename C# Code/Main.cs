using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

class Program
{
    static void Main()
    {
        var csvContent = @"
Name,Address,Note
""John Doe"",""123 Main St, Anytown"",""This is a note
with a line break.""
""Jane Smith"",""456 Oak St, Othertown"",""Another note, with a comma.""
";

        using (var reader = new StringReader(csvContent))
        {
            var records = ReadCsv(reader);
            foreach (var record in records)
            {
                Console.WriteLine($"Name: {record["Name"]}, Address: {record["Address"]}, Note: {record["Note"]}");
            }
        }
    }

    static List<Dictionary<string, string>> ReadCsv(TextReader reader)
    {
        var records = new List<Dictionary<string, string>>();
        var headers = new List<string>();
        bool isHeader = true;
        var currentRecord = new Dictionary<string, string>();

        var sb = new StringBuilder();
        string currentHeader = null;
        bool inQuotes = false;
        int currentIndex = 0;

        while (reader.Peek() != -1)
        {
            char c = (char)reader.Read();
            if (inQuotes)
            {
                if (c == '"')
                {
                    if (reader.Peek() == '"')
                    {
                        sb.Append('"');
                        reader.Read(); // Consume the second quote
                    }
                    else
                    {
                        inQuotes = false;
                    }
                }
                else
                {
                    sb.Append(c);
                }
            }
            else
            {
                if (c == '"')
                {
                    inQuotes = true;
                }
                else if (c == ',')
                {
                    if (isHeader)
                    {
                        headers.Add(sb.ToString().Trim());
                    }
                    else
                    {
                        currentRecord[currentHeader] = sb.ToString().Trim();
                    }
                    sb.Clear();
                    currentIndex++;
                }
                else if (c == '\n' || c == '\r')
                {
                    if (reader.Peek() == '\n') reader.Read(); // Handle CRLF
                    if (sb.Length > 0 || !isHeader && currentIndex == headers.Count - 1)
                    {
                        if (isHeader)
                        {
                            headers.Add(sb.ToString().Trim());
                            isHeader = false;
                        }
                        else
                        {
                            currentRecord[currentHeader] = sb.ToString().Trim();
                            records.Add(new Dictionary<string, string>(currentRecord));
                            currentRecord.Clear();
                        }
                        sb.Clear();
                        currentIndex = 0;
                    }
                }
                else
                {
                    sb.Append(c);
                }
            }

            if (currentIndex < headers.Count)
            {
                currentHeader = headers[currentIndex];
            }
        }

        if (sb.Length > 0)
        {
            if (isHeader)
            {
                headers.Add(sb.ToString().Trim());
            }
            else
            {
                currentRecord[currentHeader] = sb.ToString().Trim();
                records.Add(new Dictionary<string, string>(currentRecord));
            }
        }

        return records;
    }
}
