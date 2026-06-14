import SanctumDashboard from '@/components/SanctumDashboard';
import { worlds } from '@/lib/sanctum-data';
import { databaseIsConfigured, getTaskDocuments } from '@/lib/database';

export const dynamic = 'force-dynamic';

export default async function Home() {
  const documents = await getTaskDocuments();

  return (
    <SanctumDashboard
      worlds={worlds}
      databaseConfigured={databaseIsConfigured()}
      documents={documents}
    />
  );
}
