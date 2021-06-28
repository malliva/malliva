import { render } from '@testing-library/react';

import MarketAppDashboardUi from './market-app-dashboard-ui';

describe('MarketAppDashboardUi', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppDashboardUi />);
    expect(baseElement).toBeTruthy();
  });
});
