import SanctumDashboard from '@/components/SanctumDashboard';
import { worlds } from '@/lib/sanctum-data';
import { databaseIsConfigured } from '@/lib/database';

export default function Home() {
  return <SanctumDashboard worlds={worlds} databaseConfigured={databaseIsConfigured()} />;
}
